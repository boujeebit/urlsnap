<p align="center">
  <img src="https://raw.githubusercontent.com/0xACED/urlsnap/master/images/urlsnap.png"/>
</p>


Take full size screenshots of any website and save them for later. Great for viewing potentially malicious URLs without visiting them yourself. 

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
