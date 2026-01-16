# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk, simpledialog, messagebox
from tkinter import font as tkfont

POLL_MS = 1000  # how often to check for external changes

class MiniThunar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("T H U N A R")
        self.geometry("150x640")
        self.minsize(150, 300)
        self.current_dir = os.path.expanduser("~")

        # Platform modifier for shortcuts
        self.mod = "Command" if sys.platform.startswith("darwin") else "Control"

        # System fonts (Aqua-friendly)
        self.font_base = tkfont.nametofont("TkDefaultFont")
        self.font_bold = self.font_base.copy()
        self.font_bold.configure(weight="bold")

        # Internal clipboard for cut/copy file ops
        self.clipboard_path = None  # list[str]
        self.clipboard_mode = None  # "cut" or "copy"

        # Snapshot of current directory to detect changes
        self._dir_signature = None   # tuple for change detection
        self._poll_job = None

        self.create_widgets()
        self.load_directory(self.current_dir)
        self.start_dir_watcher()

    # ---------- UI ----------
    def create_widgets(self):
        # Top bar with "back" + (tiny) refresh
        topbar = ttk.Frame(self)
        topbar.pack(fill=tk.X, pady=4)
        self.back_button = ttk.Button(topbar, text="⬅", width=2, command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=6)
        self.refresh_button = ttk.Button(topbar, text="↻", width=2, command=self.refresh_now)
        self.refresh_button.pack(side=tk.LEFT)

        # File list (multi-selection)
        self.tree = ttk.Treeview(self, columns=("Name",), show="", selectmode="extended")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Make directories bold; files regular
        self.tree.tag_configure("dir", font=self.font_bold)
        self.tree.tag_configure("file")

        # Double-click: open
        self.tree.bind("<Double-1>", self.on_open)

        # Selection change -> update status
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.update_status())

        # Right-click / context-menu triggers
        self.tree.bind("<ButtonRelease-2>", self.show_menu)      # middle click (X11)
        self.tree.bind("<ButtonRelease-3>", self.show_menu)      # right click
        self.tree.bind("<Control-ButtonRelease-1>", self.show_menu)  # ctrl-click

        # Context menu
        accel = "⌘" if sys.platform.startswith("darwin") else "Ctrl+"
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="New Folder", command=self.create_folder)
        self.menu.add_command(label="New File", command=self.create_file)
        self.menu.add_separator()
        self.menu.add_command(label="Open in VSCode", command=self.open_in_vscode)
        self.menu.add_command(label="Open in GIMP", command=self.open_in_gimp)
        self.menu.add_command(label="Open in Inkscape", command=self.open_in_inkscape)
        self.menu.add_command(label="Open in Viewer", command=self.open_in_viewer)
        self.menu.add_separator()
        self.menu.add_command(label="Copy text to clipboard", command=self.copy_text)
        self.menu.add_command(label="Paste clipboard into file", command=self.paste_text)
        self.menu.add_separator()
        self.menu.add_command(label=f"Cut\t{accel}X", command=self.cut_item)
        self.menu.add_command(label=f"Copy\t{accel}C", command=self.copy_item)
        self.menu.add_command(label=f"Paste\t{accel}V", command=self.paste_item)
        self.menu.add_separator()
        self.menu.add_command(label="Delete selected", command=self.delete_selected)
        self.menu.add_command(label="Rename selected", command=self.rename_selected)
        self.menu.add_separator()
        self.menu.add_command(label=f"Refresh\t{accel}R / F5", command=self.refresh_now)

        # Keyboard shortcuts (global)
        self.bind_all(f"<{self.mod}-c>", lambda e: self.copy_item())
        self.bind_all(f"<{self.mod}-x>", lambda e: self.cut_item())
        self.bind_all(f"<{self.mod}-v>", lambda e: self.paste_item())
        self.bind_all(f"<{self.mod}-r>", lambda e: self.refresh_now())
        self.bind_all("<F5>", lambda e: self.refresh_now())
        self.bind_all("<Delete>", lambda e: self.delete_selected())
        self.bind_all("<BackSpace>", lambda e: self.delete_selected())
        self.bind_all("<FocusIn>", lambda e: self.refresh_now())  # refresh when app regains focus

        # ---------- Stacked Status (bottom, ttk for Aqua) ----------
        status_frame = ttk.Frame(self)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.dir_var = tk.StringVar(value="")
        self.info_var = tk.StringVar(value="")

        self.dir_label = ttk.Label(
            status_frame, textvariable=self.dir_var,
            anchor="w", justify="left", padding=(6, 0)
        )
        self.info_label = ttk.Label(
            status_frame, textvariable=self.info_var,
            anchor="w", justify="left", padding=(6, 0)
        )
        self.dir_label.pack(fill=tk.X, side=tk.TOP)
        self.info_label.pack(fill=tk.X, side=tk.TOP)

        # Keep wraplength in sync with window width
        self.bind("<Configure>", self._refresh_wraplengths)

    # ---------- Directory Handling ----------
    def load_directory(self, path):
        self.current_dir = path
        self.tree.delete(*self.tree.get_children())
        try:
            for entry in sorted(os.listdir(path), key=str.lower):
                full = os.path.join(path, entry)
                tag = "dir" if os.path.isdir(full) else "file"
                self.tree.insert("", "end", values=(entry,), tags=(tag,))
        except Exception as e:
            messagebox.showerror("Error", str(e))
        # Update snapshot and status
        self._dir_signature = self._compute_dir_signature(self.current_dir)
        self.update_status()

    def refresh_now(self):
        """Manual refresh; keeps selection if possible."""
        # Capture current selection names to try to reselect after reload
        selected_names = [self.tree.item(i, "values")[0] for i in self.tree.selection()]
        self.load_directory(self.current_dir)
        # Reselect items that still exist
        name_to_id = {self.tree.item(i, "values")[0]: i for i in self.tree.get_children("")}
        self.tree.selection_set([name_to_id[n] for n in selected_names if n in name_to_id])

    def go_back(self):
        parent = os.path.dirname(self.current_dir.rstrip(os.sep))
        if parent and os.path.exists(parent) and parent != self.current_dir:
            self.load_directory(parent)

    def get_selected_paths(self):
        sel = self.tree.selection()
        if not sel:
            return []
        paths = []
        for item in sel:
            name = self.tree.item(item, "values")[0]
            paths.append(os.path.join(self.current_dir, name))
        return paths

    # ---------- Open / Launch ----------
    def open_file(self, path):
        """Cross-platform file opener"""
        try:
            if sys.platform.startswith("darwin"):
                subprocess.call(["open", path])
            elif os.name == "nt":
                os.startfile(path)  # type: ignore[attr-defined]
            else:
                subprocess.call(["xdg-open", path])
        except Exception as e:
            messagebox.showerror("Open", str(e))

    def on_open(self, event):
        paths = self.get_selected_paths()
        if not paths:
            return
        path = paths[0]
        if os.path.isdir(path):
            self.load_directory(path)
        else:
            self.open_file(path)

    def open_in_vscode(self):
        for p in self.get_selected_paths():
            os.system(f'code "{p}" &')

    def open_in_gimp(self):
        for p in self.get_selected_paths():
            os.system(f'/Applications/GIMP.app/Contents/MacOS/GIMP "{p}" &')

    def open_in_inkscape(self):
        for p in self.get_selected_paths():
            os.system(f'/Applications/Inkscape.app/Contents/MacOS/inkscape "{p}" &')

    def open_in_viewer(self):
        for p in self.get_selected_paths():
            self.open_file(p)

    # ---------- Clipboard (Text) ----------
    def copy_text(self):
        paths = self.get_selected_paths()
        if not paths:
            messagebox.showinfo("Copy text", "No file selected.")
            return
        p = paths[0]
        if os.path.isdir(p):
            messagebox.showinfo("Copy text", "Cannot copy a folder as text.")
            return
        try:
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                data = f.read()
            self.clipboard_clear()
            self.clipboard_append(data)
            messagebox.showinfo("Copy text", f"Copied '{os.path.basename(p)}' to clipboard.")
        except Exception as e:
            messagebox.showerror("Copy text", f"Failed to copy: {str(e)}")

    def paste_text(self):
        paths = self.get_selected_paths()
        if not paths:
            messagebox.showinfo("Paste text", "No file selected.")
            return
        p = paths[0]
        if os.path.isdir(p):
            messagebox.showinfo("Paste text", "Cannot paste into a folder.")
            return
        try:
            data = self.clipboard_get()
            with open(p, "w", encoding="utf-8") as f:
                f.write(data)
            messagebox.showinfo("Paste text", f"Finished writing to '{os.path.basename(p)}'.")
            self.refresh_now()
        except Exception as e:
            messagebox.showerror("Paste text", f"Failed to paste: {str(e)}")

    # ---------- File Cut/Copy/Paste ----------
    def cut_item(self):
        paths = self.get_selected_paths()
        if not paths:
            return
        self.clipboard_path = paths
        self.clipboard_mode = "cut"
        self.update_status(msg=f"Cut {len(paths)} item(s)")

    def copy_item(self):
        paths = self.get_selected_paths()
        if not paths:
            return
        self.clipboard_path = paths
        self.clipboard_mode = "copy"
        self.update_status(msg=f"Copied {len(paths)} item(s) to clipboard")

    def paste_item(self):
        if not self.clipboard_path:
            messagebox.showinfo("Paste", "Nothing to paste.")
            return

        pasted = 0
        for src in self.clipboard_path:
            if not os.path.exists(src):
                continue
            dst = os.path.join(self.current_dir, os.path.basename(src))
            if os.path.exists(dst):
                messagebox.showwarning("Paste", f"'{os.path.basename(dst)}' already exists here.")
                continue
            try:
                if self.clipboard_mode == "copy":
                    if os.path.isdir(src):
                        shutil.copytree(src, dst)
                    else:
                        shutil.copy2(src, dst)
                elif self.clipboard_mode == "cut":
                    shutil.move(src, dst)
                pasted += 1
            except Exception as e:
                messagebox.showerror("Paste Error", f"{os.path.basename(src)}: {str(e)}")

        # clear clipboard after move
        if self.clipboard_mode == "cut":
            self.clipboard_path = None
            self.clipboard_mode = None

        self.refresh_now()
        self.update_status(msg=f"Pasted {pasted} item(s)")

    # ---------- File Ops ----------
    def delete_selected(self):
        paths = self.get_selected_paths()
        if not paths:
            return
        if not messagebox.askyesno("Delete", f"Delete {len(paths)} selected item(s)?"):
            return
        deleted = 0
        for p in paths:
            try:
                if os.path.isdir(p):
                    shutil.rmtree(p)
                else:
                    os.remove(p)
                deleted += 1
            except Exception as e:
                messagebox.showerror("Delete", f"{os.path.basename(p)}: {str(e)}")
        self.refresh_now()
        self.update_status(msg=f"Deleted {deleted} item(s)")

    def rename_selected(self):
        paths = self.get_selected_paths()
        if not paths:
            return
        if len(paths) > 1:
            messagebox.showinfo("Rename", "You can only rename one item at a time.")
            return
        p = paths[0]
        newname = simpledialog.askstring("Rename", "New name:",
                                         initialvalue=os.path.basename(p))
        if not newname:
            return
        try:
            os.rename(p, os.path.join(self.current_dir, newname))
            self.refresh_now()
            self.update_status(msg=f"Renamed to {newname}")
        except Exception as e:
            messagebox.showerror("Rename", str(e))

    def create_folder(self):
        name = simpledialog.askstring("New Folder", "Folder name:")
        if not name:
            return
        p = os.path.join(self.current_dir, name)
        try:
            os.makedirs(p, exist_ok=True)
            self.refresh_now()
            self.update_status(msg=f"Created folder {name}")
        except Exception as e:
            messagebox.showerror("Create Folder", str(e))

    def create_file(self):
        name = simpledialog.askstring("New File", "File name:")
        if not name:
            return
        p = os.path.join(self.current_dir, name)
        try:
            open(p, "w", encoding="utf-8").close()
            self.refresh_now()
            self.update_status(msg=f"Created file {name}")
        except Exception as e:
            messagebox.showerror("Create File", str(e))

    # ---------- Status / Layout helpers ----------
    def _refresh_wraplengths(self, event=None):
        wrap = max(self.winfo_width() - 10, 80)
        self.dir_label.configure(wraplength=wrap)
        self.info_label.configure(wraplength=wrap)

    def update_status(self, msg=None):
        """
        Stacked format:
          Line 1: <current directory>
          Line 2+: one selected: name\n<size or (dir)>\n<YYYY-MM-DD HH:MM>
                   many selected: "<N selected>"\n"total <bytes> bytes"
        """
        self.dir_var.set(self.current_dir)

        if msg:
            self.info_var.set(msg)
            return

        sel = self.get_selected_paths()
        if not sel:
            self.info_var.set("")
            return

        if len(sel) == 1:
            p = sel[0]
            name = os.path.basename(p)
            try:
                mtime = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
            except Exception:
                mtime = "—"
            if os.path.isdir(p):
                lines = [name, "(dir)", mtime]
            else:
                try:
                    size = os.path.getsize(p)  # raw bytes
                    lines = [name, f"{size} bytes", mtime]
                except Exception:
                    lines = [name, "—", mtime]
            self.info_var.set("\n".join(lines))
        else:
            total = 0
            for p in sel:
                if os.path.isfile(p):
                    try:
                        total += os.path.getsize(p)
                    except Exception:
                        pass
            self.info_var.set(f"{len(sel)} selected\ntotal {total} bytes")

    # ---------- Context Menu ----------
    def show_menu(self, event):
        self.tree.focus_set()
        row_id = self.tree.identify_row(event.y)

        # Preserve multi-selection if the clicked row is already selected.
        current_sel = set(self.tree.selection())
        if row_id:
            if row_id not in current_sel:
                self.tree.selection_set(row_id)
        else:
            self.tree.selection_remove(self.tree.selection())

        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    # ---------- Directory watcher ----------
    def _compute_dir_signature(self, path):
        """
        Create a lightweight signature of the directory:
        names + isdir + mtime seconds (not recursive).
        """
        try:
            entries = []
            for name in os.listdir(path):
                full = os.path.join(path, name)
                try:
                    isdir = os.path.isdir(full)
                    mtime = int(os.path.getmtime(full))
                except FileNotFoundError:
                    # raced with a change; skip
                    continue
                entries.append((name, isdir, mtime))
            entries.sort()
            return tuple(entries)
        except Exception:
            return None

    def _poll_dir(self):
        sig = self._compute_dir_signature(self.current_dir)
        if sig is not None and sig != self._dir_signature:
            # something changed: refresh view
            self.load_directory(self.current_dir)
        # reschedule
        self._poll_job = self.after(POLL_MS, self._poll_dir)

    def start_dir_watcher(self):
        if self._poll_job is None:
            self._poll_job = self.after(POLL_MS, self._poll_dir)

    def stop_dir_watcher(self):
        if self._poll_job is not None:
            self.after_cancel(self._poll_job)
            self._poll_job = None

# ---------- Run ----------
if __name__ == "__main__":
    app = MiniThunar()
    app.mainloop()
