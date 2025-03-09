# CSS Selector Cheatsheet

A quick reference for the top 10 most-used CSS selectors.

## 1. Universal Selector (`*`)
```css
* {
    margin: 0;
    padding: 0;
}
```
**What it does:** Selects all elements on the page.

---

## 2. Type Selector (`element`)
```css
p {
    font-size: 16px;
}
```
**What it does:** Selects all `<p>` elements and applies styles to them.

---

## 3. Class Selector (`.classname`)
```css
.button {
    background-color: blue;
    color: white;
}
```
**What it does:** Selects all elements with the class `button`.

---

## 4. ID Selector (`#id`)
```css
#header {
    font-size: 24px;
}
```
**What it does:** Selects the element with the `id` of `header`.
*(IDs should be unique per page.)*

---

## 5. Descendant Selector (`ancestor descendant`)
```css
div p {
    color: gray;
}
```
**What it does:** Selects all `<p>` elements inside a `<div>`.

---

## 6. Child Selector (`parent > child`)
```css
nav > ul {
    list-style: none;
}
```
**What it does:** Selects `<ul>` elements that are *direct children* of `<nav>`.

---

## 7. Adjacent Sibling Selector (`element + element`)
```css
h1 + p {
    margin-top: 10px;
}
```
**What it does:** Selects the first `<p>` immediately following an `<h1>`.

---

## 8. General Sibling Selector (`element ~ element`)
```css
h1 ~ p {
    color: darkgray;
}
```
**What it does:** Selects all `<p>` elements that are siblings of an `<h1>`, not just the first one.

---

## 9. Attribute Selector (`[attribute]`)
```css
a[target="_blank"] {
    color: red;
}
```
**What it does:** Selects all `<a>` elements with `target="_blank"`.

---

## 10. Pseudo-Class Selector (`:pseudo-class`)
```css
button:hover {
    background-color: green;
}
```
**What it does:** Applies styles when a user hovers over a `<button>`.

---

💡 *Use these selectors to build efficient and maintainable stylesheets!* 🚀

