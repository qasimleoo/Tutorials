## What is Thymeleaf?

**Thymeleaf** is a **server-side Java template engine** primarily used for building web applications. It allows you to generate dynamic HTML (and XML, JS, CSS, text) by combining static templates with backend data.

It is most commonly used with **Spring Boot** and **Spring Framework**.

In simple terms:
Thymeleaf lets you take backend data (Java objects) and render it into HTML pages.

---

## Why is Thymeleaf Needed?

When building web applications, you typically have:

* **Backend (Java)** → Business logic, database access
* **Frontend (HTML/CSS/JS)** → UI
* A need to **inject dynamic data into HTML**

Without a template engine, you would:

* Manually build HTML strings in Java (bad practice)
* Or use JSP (older, tightly coupled with servlet container)

Thymeleaf solves this by:

### 1. Separating Concerns

* Java handles logic
* HTML handles presentation
* Clean MVC architecture

### 2. Natural Templates

Thymeleaf templates are valid HTML files.
You can open them directly in a browser without a server.

Example:

```html
<p th:text="${username}">Default Name</p>
```

If no server runs → shows "Default Name"
If server runs → replaced with actual value.

### 3. Integration with Spring

It integrates deeply with:

* Spring MVC
* Spring Security
* Form validation
* Model binding

---

## Where is Thymeleaf Used?

### 1. Spring Boot Web Applications

Most common use case:

* Traditional server-rendered web apps
* Admin panels
* Internal enterprise apps

### 2. MVC Architecture

In MVC:

* **Model** → Java objects
* **View** → Thymeleaf template
* **Controller** → Handles requests and passes model data

Example:

```java
@GetMapping("/hello")
public String hello(Model model) {
    model.addAttribute("name", "John");
    return "hello";
}
```

Thymeleaf file (`hello.html`):

```html
<p th:text="${name}"></p>
```

---

## How Does Thymeleaf Work?

### Step 1 — Dependency

In Maven:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

---

### Step 2 — Template Location

Templates go inside:

```
src/main/resources/templates/
```

---

### Step 3 — Controller Returns Template Name

```java
return "home";
```

Spring automatically:

1. Finds `home.html`
2. Processes Thymeleaf tags
3. Injects model data
4. Returns rendered HTML to browser

---

## Key Features

### 1. Expression Language

```html
${variable}
```

### 2. Conditional Rendering

```html
<p th:if="${isAdmin}">Admin Panel</p>
```

### 3. Looping

```html
<li th:each="item : ${items}" th:text="${item}"></li>
```

### 4. Form Handling

```html
<form th:action="@{/save}" th:object="${user}" method="post">
```

---

## When Should You Use Thymeleaf?

Use it when:

* You are building a **Spring Boot MVC application**
* You want server-side rendering
* You need SEO-friendly pages
* You want tight integration with Spring Security & Forms

Do NOT use it when:

* You are building a SPA (React, Angular, Vue)
* You are using REST APIs only
* Frontend and backend are completely separate

---

## Thymeleaf vs JSP (Short Comparison)

| Feature            | Thymeleaf | JSP     |
| ------------------ | --------- | ------- |
| Modern             | Yes       | Older   |
| Natural HTML       | Yes       | No      |
| Spring Integration | Excellent | Limited |
| Recommended Today  | Yes       | Rarely  |

---

## Summary

Thymeleaf is:

* A Java template engine
* Used with Spring Boot
* Designed for server-side HTML rendering
* Clean, maintainable, MVC-friendly



---------------


Thymeleaf Standard Expressions

Five types:
1. ${...}: Variable expressions
2. \*{...}: Selection expressions
3. #{...}: Message (i18n) expressions
4. @{...}: Link (URL) expressions
5. ~{...}: Fragment expressions


1. ${...}: Variable expressions 

i. mostly used
ii. bind data from template context (model) into the resulting html (view)

Syntax:
${variableName}

```java
// Handler method
@GetMapping("message")
public String msg(Model model) {
	model.addAttribute("message", "Hello");
	return "message" // HTML file name
}
```

2. \*{...}: Selection expressions:

i. They are like variable expressions, except they will be executed on a previously selected object instead of the whole context varibales map.
ii. To use selection expressions you first need to define a `th:object` attribute. After that, you can use the selection expressions to select the attributes/fields of the selected object.

```html

<h2>User Details</h2>
<div th:object="${user}">
	<p>Name: <strong th:text="*{name}"></strong></p>
	<p>Email: <strong th:text="*{email}"></strong></p>
	<p>Role: <strong th:text="*{role}"></strong></p>
	<p>Gender: <strong th:text="*{gender}"></strong></p>
</div>
```


3. Message Expressions

i. let you externalize common texts into a properties file.
ii. Syntax: `#{message.property.key}`
iii. Let's say you have a welcome msg that you wanna show on every view. However, hardcoding this msg on all of these views is a bad idea.


```messages.properties 
app.name=Sample app
welcome.message=Welcome to Thymeleaf
```

```html
<body>
	<h1>Message Expression Demo:</h1>
	<h2 th:text="#{app.name}"></h2>
	<h2 th:text="#{welcome.message}"></h2>
</body>
```


4. Link/URL expressions

Syntax: `@{link}`

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.w3.org/1999/xhtml">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>

	<link rel="stylesheet" type="text/css" th:href="@{/css/demo.css}">
</head>
<body>

	<a th:href="@{/welcome}">Welcome</a>
	<a th:href="@{/message/{id}(id=${id})">Link with Param</a>
	<!-- via model attribute -->
</body>
</html>
```  


5. Fragment expressions

easy way to represent fragments of markup and move them around templates.

Syntax: ~{fragment name}

i. th:insert - inserts contect inside the tag
ii. th:replace - replaces the current tag with the tag defininf the fragment
iii. th:include: this is deprecated but it may still appear in lagacy code. Inserts only the fragment’s body (not the outer tag) .. X Deprecated (Thymeleaf 3+)


```html
<!-- /templates/common/header.html -->
<div th:fragment="head"></div>
```

```html
<!-- /templates/common/footer.html -->
<div th:fragment="footer"></div>
```

```html
<div th:insert="~{common/header :: head}"></div>

<!-- Body -->

<div th:replace="~{common/footer :: footer}"></div>
```



-------------

### th:text attribute

used to display text that is evaluated from the expression inside it:

Example: 

```html
<p th:text=${message}>Dummy data</p> 
```


### th:each attribute
##### for iteration or looping

allows different datatypes

```html
<ul th:each="user: ${users}">
	<td th:text="${user.name}"></td>
	<td th:text="${user.email}"></td>
	<!-- <td th:text="${user.name}"></td> -->
	<!-- <td th:text="${user.name}"></td> -->
</ul>
```

You can also enable a diff property .. to keep track of iteration process via the `status` variable

<ul th:each="user, iterStat: ${users}">
	<td th:text=${iterStat.count}></td> 
	<td th:text="${user.name}"></td>
	<td th:text="${user.email}"></td>
	<!-- <td th:text="${user.name}"></td> -->
	<!-- <td th:text="${user.name}"></td> -->
</ul>
```

The status variable provides the following properties:
- index -> current index - starting from 0
- count -> number of elements processed so far
- size -> total number of elements in a list
- even/odd -> checks if current iteration index is even or odd
- first -> checks if current iter is first
- last -> checks if current iter is last