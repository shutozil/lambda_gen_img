## dev

```
npm run build
sam local invoke FUNCTION_NAME --env-vars env.json --profile YOUR_PROFILE
```

## `env.json`

- template に渡す環境変数
- 環境変数がネストしているイメージ

### sam local invoke で Access Denied

```
$ sam local invoke FUNCTION_NAME --profile YOUR_PROFILE
```

https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html
