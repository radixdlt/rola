# ROLA as a Service

Deploy your own instance of a ROLA authentication as a serverless API.

## Getting started

### AWS Profile

Follow this guide to setup an [AWS profile](https://sst.dev/chapters/create-an-iam-user.html)

### Config

Populate the [config](./sst.config.ts) with your dApp values

```javascript
const config = {
  [NetworkId.Stokenet]: {
    origin: 'http://localhost:4000',
    dAppDefinitionAddress:
      'account_tdx_2_12yf9gd53yfep7a669fv2t3wm7nz9zeezwd04n02a433ker8vza6rhe',
    stage: networkConfig.networkName,
  },
  [NetworkId.Mainnet]: {
    origin: '',
    dAppDefinitionAddress: '',
    stage: networkConfig.networkName,
  },
}[networkConfig.networkId]
```

```bash
# installs node dependencies
npm install
```

```bash
# runs a test environment
npm run dev
```

```bash
# deploys your code to AWS
npm run deploy
```

## Endpoints

`POST /create-challenge`

Creates a 32 bytes hex string encoded random value.

```json
// request body
{}

// response
{
  "challenge": "052b682245a013a5cab2ce49e3d1d8dc3b3ceade02dbddb78ca487829d6a3c93"
}
```

`POST /verify`

Creates a 32 bytes hex string encoded random value.

```json
// request body
[
  {
    "challenge": "052b682245a013a5cab2ce49e3d1d8dc3b3ceade02dbddb78ca487829d6a3c93",
    "proof": {
      "publicKey": "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552",
      "signature": "62ee0e0d9839a1577289336a90d51ad1de576f392b613d961c2e9c9aca5e6f5d7cc9fdd03a17105bd8bdc124425dc7cda390bb2713e0e3cf0712c9a42c2f3400",
      "curve": "curve25519"
    },
    "address": "identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc",
    "type": "persona"
  },
  {
    "proof": {
      "publicKey": "0cc4199f056303ba4f85bea0f824f05f323f9426d66c34fda6cc30fa4dda945f",
      "signature": "a753219837f4b272f47cb35a65bf0268930fd749227c952282db1f3868b687f0d078c8cde98999bd20bfd97c6cdb6922fddc24a45317d247c54d8302d43b8105",
      "curve": "curve25519"
    },
    "address": "account_tdx_2_12yzqmuj80lcz8zudxdxeupalvq9ghv30z63s9twnwxklts8p70g3nv",
    "challenge": "052b682245a013a5cab2ce49e3d1d8dc3b3ceade02dbddb78ca487829d6a3c93",
    "type": "account"
  }
]

// response
{ "valid": true }
```

# License

The ROLA code and examples is released under [Apache 2.0 license](LICENSE). Binaries are licensed under the [Radix Software EULA](http://www.radixdlt.com/terms/genericEULA)
