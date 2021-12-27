# twitter-auth
twitter oauth1 authenticator cli

## Dependencies
The cli may require to have the following dependencies installed:

- Python3
- make


### How to run

#### Set your twitter application credentials

The application may require you to set your twitter app `consumer_key` and `consumer_secret` in a `config.ini` file.

- To do so, create a config.ini using `mv example.config.ini config.ini`
- Then replace the file `[AUTH]` fields with the corresponding values

```toml
[AUTH]
consumer_key=<a_consumer_key
consumer_secret=<a_consumer_secret>
```

#### Run the application

To run the application execute `make run`, this command will ask you for a `verifier` `PIN`. To get this `PIN`

1- Open on your browser the `auth url`.
2- Click on `Authorize App`

<img width="704" alt="Screenshot 2021-12-27 at 14 23 52" src="https://user-images.githubusercontent.com/5704817/147476015-91eaa0ea-0a99-4534-97ac-b5c979ccbb58.png">

3- then copy and paste the pin on your terminal.

 <img width="717" alt="Screenshot 2021-12-27 at 14 24 03" src="https://user-images.githubusercontent.com/5704817/147476045-46a358c9-4db5-4dac-886e-c18968e5c25b.png">

The CLI should spit out the twitter user api key and secret you can use to perform tasks on their behalf.

**Example:**
```
venv/bin/python3 main.py
auth url:  https://api.twitter.com/oauth/authorize?oauth_token=<token>
Verifier:3553107
api_key: <USER_API_KEY>
api_secret: <USER_API_SECRET>
```
