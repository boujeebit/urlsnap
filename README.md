# URL SNAP

Something Cool

## Docker Building 

```
docker build -t urlsnap .
docker run -i --rm --cap-add=SYS_ADMIN -v $(pwd)/tmp/images:/home/pptruser/images urlsnap
```