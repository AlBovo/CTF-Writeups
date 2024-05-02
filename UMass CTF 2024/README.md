# UMass CTF 2024
<p style="text-align:center">
    <img src="umass.png" name="umass logo" class="center">
</p>

## Binary
### Free Delivery


## Web
### Spongebob Homepage
This challenge didn't have attachments but only proposed a website where images were loaded through `GET` queries. By analyzing these queries more closely, I understood how they resized the requested image using **ImageMagick**. Noting this functionality, I attempted to execute an `OS Command Injection` by sending random characters (of course, it didn't work). At this point, I searched the internet until I found a known vulnerability that allowed executing arbitrary commands. Thanks to [this](https://github.com/ImageMagick/ImageMagick/issues/6339) vulnerability, I managed to extract the flag from the file `flag.txt`.

### Crabby Clicker
Crabby Clicker is a challenge that comes with a `GO` source code attachment. This implements a simple web server that parses HTTP requests and sends them to a route that simply increases a counter. 
```go
func (r *RequestHandler) handleRequest() {
	defer r.conn.Close()

	reader := bufio.NewReader(r.conn)

	for {
		// Set a deadline for reading. If a second passes without reading any data, a timeout will occur.
		r.conn.SetReadDeadline(time.Now().Add(1 * time.Second))

		// Read and parse the request headers
		request, err := readHTTPHeader(reader)
		if err != nil {
			return
		}

		requestLines := strings.Split(request, "\n")
		if len(requestLines) < 1 {
			fmt.Println("Invalid request")
			return
		}

		// Parse the request line
		requestLine := strings.Fields(requestLines[0])
		if len(requestLine) < 3 {
			fmt.Println("Invalid request")
			return
		}

		method := requestLine[0]
		uri := requestLine[1]

		// Check if the request is a valid GET request
		if method != "GET" {
			r.conn.Write([]byte("HTTP/1.1 405 Method Not Allowed\r\n\r\n"))
			return
		}

		// Handle GET request
		if uri == "/" {
			r.generateResponse(` ... `)
		} else if uri == "/click" {
			// BUG: Weird thing where the state is not updated between requests??
			r.burgers++
			r.generateResponse("burger added")
		} else if uri == "/flag" {
			if r.burgers >= 100 {
				r.generateResponse(fmt.Sprintf("Flag: UMASS{%s}", os.Getenv("FLAG")))
			} else {
				r.generateResponse("Not enough burgers")
			}
		} else {
			r.generateResponse("Not found")
		}
	}
}
```
However, to obtain the flag, it's necessary to bring the counter to a value greater than or equal to **100**. 
This seems impossible since the server forgets requests once the connection is closed.
At this point, it became clear to me how vulnerable the web server was to [`HTTP request smuggling`](https://portswigger.net/web-security/request-smuggling).
After banging my head against the wall for quite some time, I understood how to exploit this challenge using a script that sends 100 GET requests in order to bring the counter to the required value and then request the flag.

### Holesome Birthday Party
Unlike the others, this challenge **didn't require knowledge** of a specific vulnerability because the very objective of the problem was to set request headers correctly.
Specifically, these headers allowed obtaining the flag:
```json
"Date": "Sat, 14 Jul 2024 23:25:28 GMT",
"User-Agent" : "Bikini Bottom",
"Accept-Language": "fr-CH",
"Cookie" : "flavor=chocolate_chip; Login=eyJsb2dnZWRpbiI6IHRydWV9Cg=="
```