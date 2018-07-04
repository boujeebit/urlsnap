# URL SNAP

Something Cool

## Install 
- Instal Docker 
- Build image
- Install pip3 packages
- Build database

## Setup
- Add volume file

## Docker Building 

```
docker build -t urlsnap .
docker run -i --rm --cap-add=SYS_ADMIN -v $(pwd)/tmp/images:/home/pptruser/images urlsnap 'URL' 'filename'
```