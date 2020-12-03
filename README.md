# firebase-redirects-py

A tool that writes redirect information to `firebase.json` from CSV.

## Usage

```sh
% python firebase-redirects.py firebase.json redirects.csv
```

## Example 

[sample/sample-without-redirects.json](https://github.com/daisuke-t-jp/firebase-redirects-py/blob/master/sample/firebase-sample-without-redirects.json)

```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

[sample/redirects.csv](https://github.com/daisuke-t-jp/firebase-redirects-py/blob/master/sample/redirects.csv)

```csv
source,destination,type
/foo,/bar,301
"/foo{,/**}",/bar,301
/firebase/**,https://firebase.google.com/,302
/firebase/.*,https://firebase.google.com/,302
```

Run script.

```sh
% python firebase-redirects.py sample/firebase-sample-without-redirects.json sample/redirects.csv 
```

Output `firebase.json`

```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "redirects": [
      {
        "source": "/foo",
        "destination": "/bar",
        "type": 301
      },
      {
        "source": "/foo{,/**}",
        "destination": "/bar",
        "type": 301
      },
      {
        "source": "/firebase/**",
        "destination": "https://firebase.google.com/",
        "type": 302
      },
      {
        "source": "/firebase/.*",
        "destination": "https://firebase.google.com/",
        "type": 302
      }
    ]
  }
}
```
