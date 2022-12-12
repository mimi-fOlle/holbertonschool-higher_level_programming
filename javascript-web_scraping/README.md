# JavaScript - Web scraping

## Resources


-   [Working with JSON data](https://intranet.hbtn.io/rltoken/MiTgYMkQEYW7Ydfr2Enb-A "Working with JSON data")
-   [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.hbtn.io/rltoken/FaAMZnG2vwWwzlkrYrhC0A "The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco")
-   [request module](https://intranet.hbtn.io/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ "request module")
-   [Modern JS](https://intranet.hbtn.io/rltoken/ULF1RX7OyNexRK1q7qpcwA "Modern JS")

## Learning Objectives

-   Why JavaScript programming is amazing
-   How to manipulate JSON data
-   How to use  `request`  and fetch API
-   How to read and write a file using  `fs`  module

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS using  `node`  (version 10.14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/node`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be  `semistandard`  compliant.  [Rules of Standard](https://intranet.hbtn.io/rltoken/Z50ZPNHxGgFadRcaHCXWLQ "Rules of Standard")  +  [semicolons on top](https://intranet.hbtn.io/rltoken/ZDy8VNGPo5AIV8I4YAJ7nA "semicolons on top"). Also as reference:  [AirBnB style](https://intranet.hbtn.io/rltoken/VC05wFk369ONcZZR8uLtjw "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   You are not allowed to use  `var`

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://intranet.hbtn.io/rltoken/ZDy8VNGPo5AIV8I4YAJ7nA "Documentation")

```
$ sudo npm install semistandard --global

```

### Install  `request`  module and use it

[Documentation](https://intranet.hbtn.io/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

```

**Notes:**  Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
