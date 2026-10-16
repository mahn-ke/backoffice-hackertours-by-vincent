import http from 'http';

const PORT = Number(process.env.PORT || 3000);

const server = http.createServer((req, res) => {
    if (req.url === '/healthz') {
        res.writeHead(200);
        res.end('OK');
    } else {
        res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Hackertours backoffice');
    }
});

server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${server.address().port}`);
});
