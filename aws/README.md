# My AWS Blog

## Set up environment

### Create virtual env


### AWS profile/credentials
Create new profile
```buildoutcfg
aws configure --profile <profileName>
```

List configured aws profiles
```buildoutcfg
aws configure list-profiles
```

Set aws profile
```buildoutcfg
export AWS_PROFILE="<profileName>"
```

Check the current aws profile
```buildoutcfg
aws configure list
```

### Install dependencies
```buildoutcfg
npm install
```


## Deployment
```buildoutcfg
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are now available for serverless to use
```buildoutcfg
sls deploy --stage <stage>
```
'export' command is valid only for unix shells. In Windows - use 'set' instead of 'export'