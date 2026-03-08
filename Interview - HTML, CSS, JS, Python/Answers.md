This is your comprehensive answer sheet for the 200 questions. These are phrased for **oral delivery**—meaning they are concise and get straight to the point.

---

### Part 1: HTML Answers
1. **HyperText Markup Language.**
2. It tells the browser that the document is an **HTML5** document.
3. The `<html>` tag.
4. `<head>` contains metadata (title, links to CSS); `<body>` contains the visible content.
5. Using the `<a>` (anchor) tag with the `href` attribute.
6. `target="_blank"`.
7. `<img>`, `<br>`, `<hr>`.
8. `<ul>` is bulleted (unordered); `<ol>` is numbered (ordered).
9. The `<br>` tag.
10. `<table>` (the container), `<tr>` (row), `<th>` (header), and `<td>` (data cell).
11. It provides a text description of an image if it fails to load or for screen readers.
12. `<h1>` (most important) down to `<h6>` (least important).
13. `<input type="text">`.
14. To collect user input and send it to a server.
15. `GET` sends data via the URL (visible); `POST` sends data in the HTTP body (secure/hidden).
16. Using the `<optgroup>` tag.
17. Using tags that describe their meaning (e.g., `<header>` vs `<div>`) for better SEO and accessibility.
18. `<header>`, `<footer>`, `<article>`, `<nav>`.
19. Buttons have built-in accessibility and keyboard interaction (Enter/Space key) that divs do not.
20. To provide data about the page like character encoding, description, or viewport settings.
21. Using `<link rel="icon" href="favicon.ico">` in the `<head>`.
22. `id` is unique to one element; `class` can be used on multiple elements.
23. Yes, separated by spaces (e.g., `class="btn primary"`).
24. No, an element should only have one unique ID.
25. `<!-- Comment here -->`.
26. To embed another document or website inside the current page.
27. For drawing graphics on the fly via JavaScript.
28. Using the `<video>` tag with `<source>` tags inside.
29. `<b>` is for visual bolding; `<strong>` indicates the text is of strong importance.
30. `<i>` is for visual italics; `<em>` is for emphasized stress.
31. To group related content together within a document.
32. For independent, self-contained content (like a blog post or news story).
33. Give the input an `id` and the label a `for` attribute with the same value.
34. A short hint displayed inside an input field before the user enters a value.
35. Add the `required` attribute to the input tag.
36. To define a set of navigation links.
37. It opens the linked document in a new window or tab.
38. Using the `<script src="file.js"></script>` tag.
39. Just before the closing `</body>` tag (so the HTML loads first).
40. Using `<link rel="stylesheet" href="style.css">` in the `<head>`.
41. To group an image with a caption (`<figcaption>`).
42. It specifies the default value (or submitted value) of an input.
43. `Block` starts on a new line; `Inline` stays on the same line.
44. `<div>`, `<h1>`, `<p>`.
45. `<span>`, `<a>`, `<img>`.
46. To create a clickable dropdown widget that shows/hides content.
47. It identifies the language of the page for search engines and screen readers.
48. `<input type="checkbox">`.
49. `<input type="radio">`.
50. It identifies the data when it is sent to the server (the "key" in key-value pairs).

---

### Part 2: CSS Answers
1. **Cascading Style Sheets.**
2. Inline, Internal (style tag), and External (.css file).
3. The part of a CSS rule that tells the browser which HTML element to style.
4. A box consisting of Content, Padding, Border, and Margin.
5. `Padding` is space inside the border; `Margin` is space outside the border.
6. `background-color: blue;`.
7. `color: red;`.
8. `px` is fixed; `em` is relative to the parent font size; `rem` is relative to the root (html) font size.
9. `font-weight: bold;`.
10. `text-align: center;`.
11. It pushes an element to the left or right; it’s rarely used now because of Flexbox/Grid.
12. `static`, `relative`, `absolute`, `fixed`.
13. `Relative` is positioned relative to its normal spot; `Absolute` is relative to its nearest positioned ancestor.
14. `width: 100%;` or `display: block;`.
15. It controls the stacking order of overlapping elements (higher number stays on top).
16. `display: none;` or `visibility: hidden;`.
17. `display: none` removes the element from the layout; `visibility: hidden` hides it but keeps its space empty.
18. A layout model for arranging items in a row or column efficiently.
19. `justify-content`.
20. `align-items`.
21. A 2D layout system for creating complex web layouts with rows and columns.
22. By using Fluid Grids, Flexible Images, and Media Queries.
23. A block of CSS that only applies if certain conditions (like screen width) are met.
24. It includes padding and borders in the element's total width and height.
25. `font-family: Arial, sans-serif;`.
26. `opacity` affects the whole element; `rgba()` allows you to set transparency for just the color.
27. `box-shadow`.
28. `text-shadow`.
29. A keyword added to a selector to style a special state (e.g., `:hover`).
30. To apply styles when the user's mouse is over an element.
31. It styles a specific part of an element (e.g., `::before` or `::first-letter`).
32. `inline` doesn't allow width/height; `inline-block` does.
33. Set `max-width: 100%;` and `height: auto;`.
34. `vh` is 1% of the viewport height; `vw` is 1% of the viewport width.
35. `border-radius: 10px;`.
36. It allows you to change property values smoothly over a given duration.
37. Transitions trigger on state change (hover); Animations can run automatically and have keyframes.
38. The set of rules browsers use to decide which CSS rule is the most relevant.
39. An **ID** is more specific than a class.
40. `div p { ... }`.
41. It overrides all other styling rules for that property.
42. `list-style: none;`.
43. `cursor: pointer;`.
44. It hides content that is too large for its container.
45. Using `position: absolute` (or relative) and `z-index`.
46. `static`.
47. `column-count: 3;`.
48. A reusable value defined with `--name` and used with `var(--name)`.
49. Separate them with commas: `h1, h2, p { color: blue; }`.
50. Designing for small screens first and scaling up for desktop later.

---

### Part 3: JavaScript Answers
1. String, Number, Boolean, Null, Undefined, Object, Symbol.
2. `null` is an intentional empty value; `undefined` means a variable was declared but not assigned a value.
3. `var`, `let`, or `const`.
4. `let` can be reassigned; `const` cannot.
5. A list-like object used to store multiple values in a single variable.
6. `array.push(item)`.
7. `array.pop()`.
8. A collection of related data in key-value pairs.
9. `object.property` or `object['property']`.
10. `==` checks value; `===` checks both value and data type.
11. A reusable block of code designed to perform a particular task.
12. A shorter syntax for writing functions using `=>`.
13. To print information to the browser's debug console.
14. A sequence of characters used to represent text.
15. `Number("123")` or `parseInt("123")`.
16. Strings wrapped in backticks (``) that allow embedded expressions `${}`.
17. A conditional statement that executes code if a condition is true or false.
18. `for` runs a specific number of times; `while` runs as long as a condition is true.
19. Document Object Model; the browser's internal representation of the HTML page.
20. `document.getElementById('id-name')`.
21. `element.textContent = "New Text";`.
22. `element.addEventListener('click', function)`.
23. The global object representing the browser window.
24. The object representing the HTML document loaded in the window.
25. Use `event.preventDefault()` inside the event handler.
26. A function without a name.
27. A function passed into another function as an argument.
28. Determines the visibility or accessibility of variables (Global vs Local).
29. JS moves declarations to the top of the current scope before execution.
30. An object representing the eventual completion (or failure) of an asynchronous operation.
31. Pending, Fulfilled, Rejected.
32. Modern syntax to handle Promises in a way that looks synchronous.
33. Wrapping code in a `try {}` block and handling errors in a `catch(err) {}` block.
34. JavaScript Object Notation; a lightweight data-interchange format.
35. `JSON.stringify(obj)`.
36. To create a new array by performing a function on every element of an existing array.
37. To create a new array with elements that pass a specific test.
38. `forEach` just loops; `map` returns a new array.
39. Refers to the object that is currently executing the code.
40. `setTimeout(function, milliseconds)`.
41. `clearInterval(id)`.
42. `localStorage` persists after the browser closes; `sessionStorage` clears when the tab is closed.
43. `string.length`.
44. Another name for template literals (backtick strings).
45. A one-line if-else: `condition ? trueValue : falseValue`.
46. "Not a Number"—returned when a math operation fails.
47. `Array.isArray(variable)`.
48. When an event triggers on an element and then "bubbles up" to its parents.
49. `document.getElementsByClassName()` or `document.querySelectorAll()`.
50. A way to opt into a restricted variant of JS that catches common coding bugs.

---

### Part 4: Python & Data Science Answers
1. A high-level, interpreted programming language known for readability.
2. Using the `def` keyword.
3. Lists are mutable (can change); Tuples are immutable (cannot change).
4. A collection of key-value pairs.
5. Using the `#` symbol.
6. The official style guide for Python code.
7. It defines the structure and blocks of the code (instead of curly braces).
8. `append` adds one item; `extend` adds all items from another list.
9. Using `python -m venv environment_name`.
10. The package manager for Python.
11. `==` checks equality (value); `is` checks identity (same object in memory).
12. A small, one-line anonymous function.
13. A concise way to create lists using a single line of code.
14. Using `try` and `except` blocks.
15. Global is accessible anywhere; Local is only accessible inside its function.
16. A file containing Python code (functions/classes) that can be imported.
17. The constructor method used to initialize an object's attributes.
18. A library for numerical computing; used for handling large arrays and matrices.
19. An N-dimensional array, the core object of NumPy.
20. `np.array([1, 2, 3])`.
21. A library for data manipulation and analysis.
22. A 2D table-like data structure with labeled axes (rows and columns).
23. `pd.read_csv('filename.csv')`.
24. `df.head()`.
25. `df['column_name']`.
26. It provides statistical summaries (mean, std, min, max) of numeric columns.
27. `df.drop(columns=['name'])`.
28. The process of fixing or removing incorrect, corrupted, or missing data.
29. By using `df.dropna()` or `df.fillna(value)`.
30. Creating new input features from existing data to improve model performance.
31. Supervised uses labeled data (has answers); Unsupervised finds patterns in unlabeled data.
32. Training set is used to "teach" the model; Test set is used to evaluate its accuracy.
33. The most popular Python library for Machine Learning.
34. `from sklearn.linear_model import LinearRegression`.
35. When a model learns the training data "too well," including noise, and fails on new data.
36. When a model is too simple to capture the underlying pattern of the data.
37. A table used to evaluate the performance of a classification model.
38. The ratio of correctly predicted observations to the total observations.
39. Classification predicts a category (Yes/No); Regression predicts a continuous number (Price).
40. Creating static, animated, and interactive visualizations.
41. `plt.plot(x, y)`.
42. A visualization library based on Matplotlib that provides a high-level, attractive interface.
43. It trains the model on the provided data.
44. It uses the trained model to make predictions on new data.
45. A table showing the correlation coefficients between variables.
46. `df.sort_values(by='column_name')`.
47. `loc` is label-based indexing; `iloc` is integer-based indexing.
48. Using `pd.merge()` or `df.join()`.
49. Adjusting the scale of data so features have a mean of 0 and standard deviation of 1.
50. Because of its simple syntax and a massive ecosystem of data-specific libraries.

---

### Bonus: Oral Coding Logic
1. **Answer:** "I'd use a for loop with a range from 1 to 11 in Python, or a for loop starting at i=1 while i<=10 in JS."
2. **Answer:** "I’d select the button, add an event listener for 'click', and inside that function, set `document.body.style.backgroundColor = 'red'`."
3. **Answer:** "I’d sum the list using the `sum()` function and divide by the `len()` of the list."
4. **Answer:** "In Python, I’d use the `if 'John' in list:` syntax. In JS, I’d use `list.includes('John')`."
5. **Answer:** "I would calculate the median of the existing ages and use `fillna()` to replace the missing values with that median."