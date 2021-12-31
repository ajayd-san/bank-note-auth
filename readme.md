# Bank Note Authenticator

Hey, getting the project up and running is easy with docker. Make sure you have it installed.

## Steps -

- clone this repo using `git clone https://github.com/default-303/bank-note-auth.git`
- Run `docker build -t note_auth .`, feel free to change the name!
- Now, run `docker run note_auth`

### voila!! you have the app up and running!!!

- Now follow the local URL printed in your terminal, and paste it in your browser. Make sure to append `/apidocs` at the end of the url to go to the UI part.
- Now, enter the required values for your bank note and get the prediction for it authenticity. Remember `[0]` means fake and `[1]` means legit!!

To Stop the web app - 
- open another prompt and do `docker ps`, note the `CONTAINER_ID`.
- Run `docker stop {CONTAINER ID YOU COPIED}`
