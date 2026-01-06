# RESOURCES

Collection of notes, examples and scripts for servers, DevOps and web development.

## Top-level content

-   Text notes: AWS, Nginx.txt, Redis.txt, Tomcat.txt, clickhouse.txt, firewall.txt, proxy*reverse_proxy_vpn.txt, web_socket.txt, ftp.txt, scp.txt, sharding*&\_scaling.txt, redux.txt, regex, Error Types.txt, hypertext_hypermedia.txt, edge_runtime---Automation_tools.txt, apache_web.txt
-   Guides: webpack-turbopack-vite-babel.md, bundlers/bundlers.txt
-   Code/examples:
    -   NodeJS/ — Node examples, package.json, sample servers and a detailed ReadMe.md
    -   ShellScripting/ — many bash scripts and small projects (archive, monitoring, user creation, redaction, awk examples)
    -   webworker/ — simple web worker example (index.html, script.js, worker.js)
-   Misc: NextJS, Clickhouse notes, `.git/` (repo history)

## Quick start / usage

-   Browse notes: open any _.txt, _.md files with your editor.
-   NodeJS examples:
    -   cd NodeJS
    -   node httpServer.js (or node website.js / node index.js)
    -   If dependencies missing: run npm install (package-lock.json and node_modules are present)
-   Run shell scripts:
    -   cd ShellScripting
    -   bash 01_basic.sh (or chmod +x script && ./script.sh)
-   View webworker:
    -   Serve directory (recommended): python3 -m http.server 8000
    -   Open http://localhost:8000/webworker/index.html

## Notes

-   Many files are reference notes and examples — search the repo for specific topics:
    -   grep -R "keyword" .
-   NodeJS contains a full node_modules tree; consider running npm ci if you want a clean install.

## Contributing / maintenance

-   Add new notes under top-level or appropriate subfolders.
-   Keep large binary files out of the repo; commit only sources/notes.

## License / attribution

-   Check individual files for license headers. Add a LICENSE file if a project-wide license is needed.
