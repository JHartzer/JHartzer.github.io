# jekyll-site

TODO: Update build commands. Currently only tested inside devcontainer

```bash
docker build . -t jekyll-env
```

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -it jekyll-env jekyll build --incremental
```

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll-env jekyll serve --watch
```