# issue-example-fern-python-sdk-bug

> [!NOTE]
>
> The repo is used to reproduce the bug of the fern python sdk generated code. Part of upstream repo: https://github.com/StrayDragon/dify-openapi
>
> will archived or deleted in the future after the issue is fixed (https://github.com/fern-api/fern/issues/6293)

The `process_rule` field in `UpdateDocumentByFileRequestData` cannot be used, otherwise an error will be reported.



## Version

```bash
$ fern -v
0.56.5
```

- python generator version [./fern/generators.yml](fern/generators.yml)
- python sdk deps version [./pyproject.toml](pyproject.toml)

## Reproduce

```bash
0. ensure `uv` is installed
1. uv sync
2. uv run server.py
```

- run client

```bash
uv run client.py # Got error
uv run client.py 1 # Got correct result
```

- compare with correct result client (curl)

```bash
bash client.sh
```

## Error
```bash
TypeError: Invalid type for value. Expected primitive type, got <class 'dict'>: {'name': 'test_name', 'indexing_technique': 'high_quality'}
```


## Workaround

```bash
TARGET_FILE="src/dify_sdk/documents/client.py"
rg --passthru -N '"process_rule": process_rule' -r '"process_rule": process_rule.model_dump_json() if process_rule else None' $TARGET_FILE  > tmp.txt && mv tmp.txt $TARGET_FILE
```


## Related

- https://github.com/encode/httpx/discussions/3118