---

Sec 1: Intro

Babel
RSC

Client vs Server
Production mode .. build
Strictmode - Twice log
Ctrl shift p
Bundler - webpack
Interactivity... useClient
Hydration error
SEO
React v next
React static .. next dynamic

---

Sec 2: Rotuing

routing .. nested routing (how)
entry point - layout
is the function name important for a default react comp?
anchor vs Link
page names case sensitive?
dynamic routing

dynamic routing (hard coded?)
props (simple obj sync) - searchParam and param (promises - async)
destruct directly or using props
searchParams ? (query params)
await ? async ? props allow it?
slug
params inside a [slug] comp ..
getting slug name (destruct params it self or access using dot)

nested dynamic routes
example
(parent) params in nested route
1+ level routes
we get access to parent and child params both

catch all routes - does it affect other routes that are already there
what's in the params?
how much nesting?
required vs optional catch all
optional chaining operator
optional catch all at root level - how to allow it at root

Layout
requires html/body
ctrl + shift + R
inline styling?
more than one layouts? layouts in inner file paths (avoid <html> in inner layouts
semantic divs

metadata api (avoid using head, title, meta tags directly - use api)
export metadata comp from layout (applies to all routes) or page itself (applicable to related route only)
if you have metadata var in both .. same file overrides layout one
template and default values in title metadata %s (get from page.js metadata and append with layout.js ones title: {template: '%s | Web', default: 'Web'}

how to make dynamic metadata? for dynamic pages ..
generateMetadata .. takes {params}
absolute in title (to override the whole title even of layout that was set using %s

-   you can add all other seo/meta tags here like desc

custom 404
next built in notFound() from next/navigation
not-found.jsx - custom
more than one - allowed in sub pages

getting path name in not-found - can't use params .. have to make it client side with usePathname()

Route groups ()
jsx fragment <>
cache?
own layouts.. metadata etc.. in groups

Private folders \_
page.js is required to make a page as route
https://www.ascii-code.com/
to enforce a page with udnerscore we can use URI encoded value (% hex)
URI - special chars to hex ascii

{{}}
const myStyles = { color: 'red', fontSize: '16px' };

<div style={myStyles}>
  Hello World!
</div>

which typpa routes we covered till now?

adv - parallel and intercepting routes
parallel routing
https://www.youtube.com/watch?v=05jrkY2UuxQ
@slots to make sections in the same page using layout

Intercepting routes
https://www.youtube.com/watch?v=00v5W01qHAM
(.) same level (..) one level above (..)(..) two level above (...) from root app dir

---

Sec 3: Rendering Paradigms
Express - SSR
React - CSR
Next - 4 (all)

server side in early 90s 20s
client was introduced after .. 1st framework was angular than react, vue
website/web-app
CSR | SSR - SSG and ISR
vite??
dev mode .. all files - no bundling
prod mode.. only a few files that are needed (in both csr and ssr)
\_rsc comes for only pages that are behind the scenes .. for current page server sends html itself.. you can modify rsc files in .next/server and see the behaviour by directly accessing a file or indirectly thru links

next ... loads rsc data of those links that are visible in the screen
rsc is loaded using fetch (with x-component as content-type)

reconciliation
virtual dom
diffing (get the difference bw two things) algo
console.dir (to get as object)
const h1_virtual = <h1>Hello</h1> # simple properties
const h1_real = document.createElement('h1'); # detailed properties
h1_real.innerText = 'Hello'

'cause of diffing .. react always creates virtual dom
to see virtual dom .. you can console component name (as in SSR)
computing/doing diffing of virtual doms is called reconciliation

static/dynamic rendering
server side/ client side (on these rendering - both)
~ npm run build (o, f) console runs (static vs dynamic)
build time vs run time

SSG - making pages at build time
export function generateStaticParams() {
return [{id: 1}, {id: 2}] // using jsonplaceholder as example for many pages
}
build will take this function and make pages outta of it (filled circles on build pages)

for first request. dynamic pages are generated and placed inside ssr for ssg pages
to stop this from happening we can do `export const dynamicParams = false;`
in dev all pages are dynamic .. no static page
it will start giving 404 for new dynamic pages

ISR extended version of SSG
routes/pages where we do SSG can be ISR
once a page is made using SSG can't be refereshed with new data unless we rebuild it .. But we can regenerate using ISR after some time using a varible like
dynamicParamas .. revalidate (regenrate) default is false
`export const revalidate = false` // never regenerate - at whole page level
`export const revalidate = 5` // regenerate after 5s when a user comes
remains same for the time but when user comes it revalidates after given time and regenerates page and shows update content on next reload .. not on same

can pass in fetch .. fetch('endpoint', {next: {revalidate: 5}}) // works at fetch level

Rendering static pages - dynamically
by default static pages without [] names are statically rendered and with [] are dynamically rendered .. we can force static to be generated dynamically too
like consoling anything in static runs once on build .. never again.. to make dynamic
`export const dynamic = "force-dynamic"` // auto (based on other methods) | force-static (even using other methods) | error (if other methods are used - throw)
there are more methods there to make a page dynamic
Another method to make dynamic is getting searchParams in fun ({searchParams})
just passing keeps it client side .. you have to await and consume it to make dynamic - other methods are
using cookies/headers from next/headers
fetch with revalidate: 0 .. fetch without caching no-store

Streaming (high speed flow of data whenever it is ready rather than storing and sending in one go)
Suspense (wrap the code that will take time) .. data will be fetched in streams
always wrap promise/fetch api inside a suspense
try a loader comp with children .. like layout you can pass children
<Loader children=''Str"/> // OR
<Loader>Str</Loading>

Client Components vs Server Components (By default they all are server ...rsc)
server ones executes only on server but client ones render on both - first on server then code is sent to browser (anything that can be done on browser only - window)
server clg doesn't show on browser unlike dev mode
"use client" // called directive - whole page becomes client side - Top of file
SourceMaps (shows jsx otherwise compiled code)- for debugging
clg(window) error on server .. "use client" error on server .. use check typeof
"use strict" // for strict rules
wanna make anything client side Make a seprate comp instead of making whold page client side

Hydration processing
adding interactivity to our pre rendered pages (event listeners)
anchor tags/links are also event listeners
hydration errors - when server sent html doesn't match client

hydration error can be created using typeof (returns a string) for window in client component .. will show even in prod mode (html will be seen being changed)
slow internet and see the issue - also throws error in console ..
Date.now() Math.random() .. which will change causes hydration error

---

Sec 4: Data Fetching and State Management

Data Fetching (differs in client vs server components)
Client component
like fetching in useEffect will be client side obviously
Server component
fetch api on fucntion level (it's not js one it's exteneded version with extra things)
cache, revalidate

Loading state using
loading.jsx or wrap inside Suspense (used for blocking comps) // when to use what
Use slow apis with multiple suspense .. (suspense work on comps) .. for parallel fetching
loading .. works on whole page - (don't wanna breakdown) .. here fetching becomes sequential if we don't handle it.. 'cause we are using await for each fetch ..
to solve this we use Promise.all([all fetches]).. with a single await
you need to await twice with data here one for fetching and other for json
or you can make a function .. remember are for parallel

Rendering Server components inside client components as SSR
strict mode (twice clg 'cause runs on server and client both)
pass your child as props and it will render as server

Server Actions (asynchronous functions that run securely on the server, allowing you to handle data mutations, form submissions, and database interactions directly from your React components without the need to create separate API routes)

The Wrangler CLI is the command-line interface for the Cloudflare Developer Platform, primarily used to create, develop, test, and deploy Cloudflare Workers and Cloudflare Pages projects. (for /api/ routes) npx wrangler pages dev . .. make fucntions/api outside app
Context API - Redux (state management across all comp/pages) can't be used on client components only
context/\_\_\_\_Context.jsx // at root level - outside app
wrap layout in provider and use context in any component

---

Sec 5: Error Handling

1 - STDOUT | 2 - STDERR
npm start > server.log // Same as: npm start 1> server.log | only standard output
npm start > server.log 2>&1 // send STDERR/2 to where STDOUT/1 is going
npm start 1> server.log 2> error.log // separate
Discard
npm start > /dev/null | npm start 2> /dev/null | npm start > /dev/null 2>&1
Run in background like a daemon but closes when terminal dies
npm start > server.log 2>&1 &

error.js to handle erros - needs to be client comp
export default function Error({ error }) // can't be arrow function
// error.message | error.digest | error
nested error handling by making a error.js gloablly or on parent

Recovering from erros (un predictable case)

1. ask user to reload .. // not recommended
2. give a btn with window.location.reload() // not recommended
3. useRouter from next/navigation with reset() inside startTransition(() => {reset(); router.refresh()}) // recommended

Error handling in nested routing
making an error.js in parent will handle erros of parent as well as childrens'
but error.js in parent will override the layout.js of children as it will have higher order .. otherwise inside childrens layout.js will have higher order than of the same children level error.js
But what if there is an error inside layout.js.. in this case we will have to move error.js boundry at upper level .. in above atleast one parent level
How to handle error of root level layout.. we use a global error handler for that

Handling Client Side Exceptions
till now we have seen SSR errors .. as the errors were being thrown on server code (inside SSR code) .. happens when there is issue in rederning not console errors - needs to hard reload for other pages
So wheh CS (not rendering error) throws/causes error .. out whole page doesn't go blank .. it just shows error in console (dev and prod mode both) or as a notification (in dev mode)
there won't be any error on server - not a critical error
But let's throw a client side RENDERING error .. here we don't have Digest property
<button onClick={() => setFruits(null)}>Set to null</button>
erros.js handles both sides errors (client and server)
we use {error, reset} inside props of error.js component
To hanlde CS errors we can only reset (as props) .. no need to useRouter or startTransition

Global error handling (at root level) - global-error.js at root level
error.js won't work for root layout .. for that next js provides global-error.js .. this has higher level than layout so we need to provide html/body to it alonge with error handler
global handler just shows the error in dev mode... to see error page we habe to build and start .. try to keep minimal code here as much as you can

---

Sec 6: Styling

Global styles and CSS Modules
suppose we import a file in index as ./home.css and it has styles .. once loaded will be applied to all pages matching tags (body, p, h1, etc..) .. unless we hard reload

React CSS Modules
normally .. importing a css file to any page applies to all components .. or all tags whereever they are present in the page .. what if we wanna apply only to component where it is being imported
we have to make files as \_\_\_.module.css and not import as simpel `import file.css` but `import anyName from file.module.css` and anyName is object with a unique class name of style .. to use we do className = {anyName.proprty}
to access dash separated properties like btn-cls we use className=anyName['btn-cls'] for multiple classes we use list and join .. className={[anyName.cls1, anyName.cls2].join(' ')}
styles applied to tags are applied actually no need to access them via imported object
you can destructure the style direclty while importing like `import {title} from file.modulde.css` // not recommended

SCSS (sassy cascading style sheets) uses brackets to styles ... SASS (Syntactically Awesome styles sheets) uses spaces for identation
to `import './style.scss'` we need `npm i --save-dev sass` (to run in dev as in prod sass/scss auto converts to css)
can also sass/scss as module

Setting up Tailwind
no tailwind.config.js in version 4 .. we have to setup in css .. to add anything custom we used this file .. and inside extend.. writing outsie extend would overwrite exisiting tailwind properties

Setting up tailwind in an existing project
https://tailwindcss.com/docs/installation/framework-guides/nextjs

Image optimization using next/image
https://nextjs.org/docs/app/getting-started/images
quality={} // attribute to manage quality.. decrease initrisic size of image
adds `srcset` for responsive screens .. based on next deviceSizes defined .. picks closest and sets in srcset
try to set highet based on width .. to persist the aspect ratio (set width in img not Image and get required highet)
unoptimized - to disallow compression

on default nextjs doesn't allow external images with https or any other protocol .. we have to allow in `next.config.mjs` file
images: {
remotePatterns: [{
  hostname: 'images.unsplash.com' // website hostname - allows regex
  protocol: 'https' // or any other
  pathname: '/path1/path1x'
  },
  // more websites  
]}

another attribute is `loader` that gets props loader={(props) => {console.log(props)}} .. needs to be client side
loader={({src, quality, width}) => {
return "src" // for src where we control everyhting from external srcs like s3 bucket, cdn, cloudnary
}}

behind the scenes Image/nextjs uses sharp library to optimize images

---

Sec 7: Backend
api routes -> renamed to -> route handlers



------------------------------------------------------------------------------------------------------------------------------------------------

Caching directives

we use 'use cache' to cache any page or component

1. `cacheComponents: true` - for static content

In `next.config.ts` we add `cacheComponents: true` nextConfig root which allows caching

now to use it we need to mention components that needs to be cached or not
for caching we add 
"use cache" // at top - mostly for static

and for dynamic pages we have to wrap component inside Suspense boundary - make a layout with dynamic component


But if you try to cache a page which uses cookies or something .. it won't allow .. so to handle the data is dynamic and also uses cookies we can use:


2. `use cache: private` - for dynamic data that is user specific

uses to allow using runtime apis like cookies, headers, searchParams, etc..
you don't have to put it at top .. you can use it inside the function itself using cookies


3. `use cache: remote` - for dynamic data that is shared across users
this directive enables caching of shared data in dynamic contexts where regular cache won't work, for example after calling `await connection()`, `await cookies()`, `await headers()`

This actually on server side (not specific to users) unlike cache: private that is specific to users


// cache that is saved in above all is actually dropped or isn't on restarting the server - what if we wanna use our own cache that isn't in-memory like above .. 

4. cacheHandlers
// in next.config.ts add inside nextConfig

cacheHandlers: {
  analytics: require.resolve('./cache/file.ts'), // your file name that has implementation of caching
}

// you don't need it as built in works well but this is for custom like redis, etc... 




Hooks


// Calling setter multiple times
// Functional Updater

// useEffect helps us handle the side effects inside our components -
// help us handle the lifecycle of a component .. what happens on first render .. what happens when a comp's state is actually changed

// try a console.log inside useEffect without dependency array and you will see .. it print every time a change happens inside the component like (button click, input etc...)
// but we don't wanna print it every time .. so we use useEffect with an empty dependency array it will render only the first time

// Now if you want to change the state or console only when we click count but not when we input anything.. just add the `count` var name inside the dependency array and you will see the magic here

// dependency array => is actually the value we put inside the useEffect after our arrow function .. to trigger the things on any particular change

// cleanup function
// runs when we actually unmount a component .. like using a toggle

// useEffect's real example is actually Data fetching

/**
 * 
 * 

✅ useEffect vs useLayoutEffect
1. When they run
🔵 useEffect

Runs after the browser has painted the screen.

Runs asynchronously, after the render is committed.

Does not block the UI.

👉 Best for most side effects.

🟣 useLayoutEffect

Runs synchronously after React calculates the DOM but before the browser paints.

Blocks the paint until it finishes.

Useful for DOM measurement or syncing layout.

👉 Use only when necessary to avoid blocking UI.

2. Common Use Cases
🟦 useEffect – Typical use cases

Fetching data (API calls)

Subscribing/unsubscribing to events

Updating state that does not affect layout

Logging

Setting timers (setTimeout, setInterval)

Anything that doesn’t require DOM measurement

Example:

useEffect(() => {
  fetch("/api/users").then(...);
}, []);

🟪 useLayoutEffect – Typical use cases

Measuring the DOM (width, height, position)

Synchronously applying style changes to avoid flickering

Animations that require the layout to be known before paint

Adjusting scroll positions immediately after render

Example:

useLayoutEffect(() => {
  const rect = ref.current.getBoundingClientRect();
  console.log(rect);
});


Here you need layout info before browser paints.

⚠️ Performance Notes
useEffect

✔ Doesn’t block the page
✔ Better for performance
✔ Recommended default

useLayoutEffect

❌ Blocks browser paint
❌ Can cause jank if overused
✔ Use only when you need synchronous DOM updates

💡 Easy Rule of Thumb
If you need to… Use
Measure layout or avoid flicker useLayoutEffect
Run normal side effects (fetching, logging, subscriptions)  useEffect
🔍 Example Difference
Using useEffect

The user may briefly see incorrect layout → flicker.

Using useLayoutEffect

Runs before paint → no flicker.

**/

/**
 *
 * useRef
 * is a react hook that gives you a mutable object .. which doesn't cause re-render.. UI never updates but the updated values remains consistent
 *
 * it's like you use document.querySelector and do the things like focus.. change color etc.
 *
 */

/**
 *
 * useContext
 * helps us to maintain/persist the state across our components .. like passing a state from one comp to another one
 *
 * like we can simply pass a state value that was set using useState from parent to a child .. it will work fine but the problem rises when we have to pass the same state from parent to child to grandchild and so on
 * this is what we call as props drilling
 * and
 * to handle/avoid the situation we actually use context api or useContext hook .. that will safely allow us to pass/use value of grand parent to any child ...
 */

/**
 * useReducer
 * ideal solution to work with the states
 * works like a reduce function in js .. takes a lotta things and returns a single thing
 *
 * useReducer
 * make a function (named of your own choice) that will
 * take 2 things .. state/value (to be manipulated) and action/function
 *
 * and then use pass that function inside useReducer (funcName, defaultValue)
 *
 * const [count, dispatch] = useReducer(funcName, 0)
 *
 * you can replace dispatch with your own function (name)
 *
 * you can make a cart (add, remove, calc, empty cart etc)
 *
 *
 * real use-case can be .. to use it with context api - as they combine to behave like redux
 *
 */

/**
 * 
 * 
 * 1. What Is Memoization?
 * 
 * Memoization is an optimization technique in computer science that caches the results of expensive function calls so that when the same inputs occur again, you can return the cached result instead of recomputing.
 * 
 * Key points:
    It maps arguments to results.
    It avoids repeated computation.
    Useful when a function is pure (i.e., same inputs always produce same output).
  
  * For example: an object containing the key: values with square of numbers .. don;t have to calc again and again .. just make once and store in an object and get from that every time you need one


  2. What Is useMemo?
  useMemo is the React hook for memoizing values within a component render.

  Purpose:
    Avoid recalculating a derived value unless its dependencies change.
    Helps performance when a calculation is expensive.
    
  Signature:
    const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

  How it works:
    On first render, computes the value.
    On subsequent renders, returns the cached value if dependencies haven’t changed.
    If dependencies change, it recomputes.

  When to use:
    Expensive transformations.
    Avoiding recalculation on every render.
  
  Bad use case (not necessary):
    const x = useMemo(() => 2 + 3, []); // pointless calculation



  
  3. What Is useCallback?
    useCallback is the React hook for memoizing functions passed to child components or used in effects.

  Purpose:
    Prevent function identity from changing on every render.
    Helps avoid unnecessary re-renders in child components that depend on reference equality.

  Signature:
    const memoizedCallback = useCallback(() => {
      doSomething(a);
    }, [a]);

  How it works:
    Returns the same function reference unless dependencies change.

  Example:
    const handleClick = useCallback(() => {
      setCount((c) => c + 1);
    }, []);

  This prevents re-creating handleClick on every render.




 */

/**
 * useImperativeHandle
 * we can pass props from parent to child .. but can we pass them from child to parent .. yes we can.. using useImperativeHandle hook
 *
 * you can make a child comp .. where you have to highlight the input using a ref .. but use the reference in your parent component
 *
 *
 */

/**
 * useId
 *
 * used to create random ids.. you can take example of id link for an input in a checkbox/radio cases
 * just use `const id = useId()` and it will give you a random id
 *
 */

/**
 * useTransition
 * used when you have to add a transition on a data that will take time to load .. or can lag the system.. like API Calls.. it marks the data as non-urgent so that other parts keep working correctly
 *
 * just use
 * const [isPending, startTransition] = useTransition
 *
 * isPending for Loading.. state and put the to be calculated inside startTransition
 *
 */

/**
 * UseDeferredValue
 * similar to useTransition but has a diff use case
 * it doesn't show loading instead it shows the previous calc value when the new when is being loaded
 */

/**
 * useState
 * useRef
 * useEffect
 * useEffectLayout
 * useContext
 * useReducer
 * useMemo
 * useCallback
 * useImperativeHandle
 *
 * useId
 * useTransition
 * useDeferredValue
 *
 * useActionState - for form submission
 * useFormStatus (from react-dom not react) - for getting form data in child comps without passing them as props..
 *
 * useOptimistic - used to show a placeholder for the data when it is being sent and will get some response back .. like insta msgs
 */



---
---
---

Section 07: Backend

apis, rest apis, CRUD operations, storing data in databases, authentication (who you are) vs authorization (what you can do)
(GET, POST, TRACE, HEAD, PUT)

older versions: api routes just like pages router
newer versions: route handlers just like app router

Backend code: How do we run OR how does it run? 

- Frontend page: `page.js` under a directory 
- Backend api: `route.js` under the directory
same directory can't have both (in old versions route had priority)

Changing port: 
`npm run dev -- -p 3300`

Or update in packages.json 
`npx dev -p 3300 `


route.js needs code with request type (GET, POST, etc) 
you can add a console.log to test 


Import diff:

ES5: 
```js
var module = require('./module-file');
```

ES6: 
```js
import defaultExport from './module-file';
```

ES5 (2009) is the older, widely supported standard of JavaScript, while ES6 (2015)

```js
console.log(a);

var a = 5;
```

- var -> let, const
- function -> () => {}
- modules -> import/export
- classes 
- promises to reduce callback hell


```bash
npm install fs
```

```js - route.js
// writefile 
// const { writeFile } = require("fs/promises");
import { writeFile } from "fs/promises";

const fileName = "hello.txt"; // will be created at root level
await writeFile(fileName, "Hey, wassup?");

console.log("\n---------\n")
console.log(`Written to file ${fileName}`);

// to check working path
console.log(process.cwd());
console.log("\n---------\n")
```

can run above code in `page.js` as well 'cause it is sever component which allows `fs` to run on server


```bash
npm install fs
```

```js
import { readFile } from "fs/promises";

const content = await readFile(fileName, "utf-8");
console.log(content);
```


UTF-8: Use for HTML, web APIs, JSON, text files, and Linux/Unix systems.
UTF-16: Use when working with Java internal strings, Windows APIs (UTF-16LE), or legacy Windows/COM applications. 



```bash
npm install http
```

```js
// Starting http server
import http from "http";
const httpServer = http.createServer((request, response) => {
    console.log(request.url);
    response.end("New Server");
});

httpServer.listen(8000, () => {
    console.log("Listening on port: 8000");
});
```

We don't do this but can do in `node.js`

in Node.js you don’t have a “magical global listening API.” You must explicitly create a server object and tell it to listen.

You need an HTTP server in Node.js because it allows your application to listen for and respond to HTTP requests over the network.



Next JS has built-in functions for HTTP Resuqests like get, post, patch, put, options, 


URL, URI, URN 

## HTTP
### HTTP Headers - metadata (in request and response)

Request Headers: from client side
Response Headers: from server side (status code convention)
Representation Headers: encoding/compression (gzip, zip, tar)
Payload (fancy name for data) Headers: data
and many more like security ones

### Most common headers:
Accept: application/json
User-agent: which app sent the reqeust (postman, chrome, mbl, safari)
Authorization: Bearer token <>
Content-type: images
cookies: key-vals (log in details)
cache-control: time to cache the data


### CORS: 
Access-control-allow-origin: 
Access-control-allow-credentials: 
Access-control-allow-method: 

### Security policies 


### HTTP methods: basic ones
GET: retrieve data
HEAD: no msg body (response headers only)
OPTIONS: what operations are available
TRACE: loopback test (get same data) - debugging (stages)
DELETE: remove
PUT: replaces an object
PATCH: particular things to update
POST: interact with resourcse (adding)


### Status codes:
1xx informational
2xx Success
3xx Redirection
4xx Client Error
5xx Server Error

#### Common ones:

100: Continue
102: Processing
200: OK- sucess
201: Created
202: Accepted
206: Cached response
210: Partial Response
301-307: Temporary redirect
302-308: Permanent redirect
400: Bad request
401: Unauthotrized
402: Payment required
404: Not Found
500: Internal server error
504: Gateway timeout



----

## Todos (CRUD Operation) A rest api endpoint

#### Get Route Handler 

```js - GET
export function GET() {
    console.log("Running get function");
    return new Response("Hello"); // JS function - try in terminal or vanilla JS
}

// OR
import { NextResponse } from "next/server";

export function GET() {
    console.log("Running get function");
    return new NextResponse("Hello");
}


// Pretty print
return new Response(JSON.stringify({ name: "Qasim" }), {
    headers: {    
        "Content-Type": "application/json", // default - text/plain

        // "Content-Type": "video/mp4",
        // "Content-Type": "audio/mp3",
        // "Content-Type": "image/png",

        // Search mime types on wikipedia or mdn
    },
    // status: 200,
    // statusText: "Your text",
});

// OR replace with 
// Response.json(jsonData) // sets header and stringifies

// in next js status code can be from 200 - 599
```


```js
import jsonData from '/path/file.json'

import jsonData from '/path/file.json' with {type: "json"}
```

--

We need to stringify JSON (using JSON.stringify()) to convert complex JavaScript objects or arrays into a plain text string format. This process, known as serialization, is essential because data must be converted into a linear text string to be stored, transmitted, or interpreted by systems that do not understand JavaScript's in-memory object structures. 


Network Transmission (API Requests): When sending data to a web server (e.g., in a POST or PUT request), HTTP only understands plain text, not JavaScript objects. JSON.stringify() transforms the data into a string that can be easily transmitted over HTTP.
LocalStorage/Cookies



#### Dynamic route handlers

`path/[id]/route.js`

2nd arg in params

```js
// export function GET(request, context) {
// export function GET(_, context) {
// console.log(context);
// export async function GET(_, {params}) {
//   const vari = await params;
export async function GET(_, {params}) {
  const {id} = await params;
  console.log(id);

  const todo = todos.find((todo) => id === todo.id.toString());
  if (!todo) {
    return Response.json(
      {error: "Not found"}, 
      {status: 404}
    );
  }

  // Response.json(data[id - 1])
  Response.json(todo);
}
```


#### Understanding Request Object - S07E04

Each route handler's first param is request object
request object in JS

```js
export async function GET(req) {
  console.log(req);
}
```

```console
> Request

> const res = await fetch('https://example.com', {
  method: 'POST',
  body: JSON.stringify({name: "Qasim"})
})

# bts it makes a request obj to call the api.. or make request

> await res.json()
```


```console
> const req = new Request('https://example.com')

> const res = await fetch(req)

> await res.json()
```

https://youtu.be/XnIfUu3TLos?t=495