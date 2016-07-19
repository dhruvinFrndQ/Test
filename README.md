# Test  Django Rest Framework
Django Rest Framwork is  used as REST API service framework, intention is to use mod_python to control freeswitch calls/scenarios and 
take input from Rest Interface over Django Rest framework.
Django REST is and easy to use model view based REST API framework with Python interface.

In the  source attached following REST API scenarios has been created.
1) outbound call with "service" as conference
2) outbound call with "service as play
3) JSON input and JSON output
4) JSON Error when service not specified.

Test the scenarios with following curl commands on test server

curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/calls/ -H "Content-Type:application/json" -d '{"destination":"testplivo1","service":"conference"}' -X POST
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/calls/ -H "Content-Type:application/json" -d '{"destination":"testplivo1","service":"play"}' -X POST

freeswitch installation had an missing "_freeswitch" file due to which freeswitch import fails

Above two scenarios reads the json from request and process the output accordingly as defined in the Test.

FreeSwith conference and Play execution from REST API have been successfully done with mod_verto using form where we use freesswitch mod_lua 
and ESL.

refer to github repository https://github.com/dhruvinFrndQ/RestAPI for REST API based outbound call execution using Post (form) request.

Note if not for "_freeswitch" module the REST API (JSON) integraion for outbound call is completed.

