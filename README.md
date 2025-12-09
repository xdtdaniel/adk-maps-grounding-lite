# adk-maps-grounding-lite
Demo of integrating Maps Grounding Lite with ADK


## Documentation

https://developers.google.com/maps/ai/grounding-lite

## Configure Environment

```bash
$ python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

Replace the API key value `PLACEHOLDER` in .env file with your actual API key.

## Run the Agent

```
$ adk web
```

## Example Query

1. What is the weather in Los Angeles?
1. Recommend me some restaurants in Mountain View.
1. What is the walk ETA from SF Caltrain station to Chase Center?
1. I am planning a trip to Los Angeles tomorrow. Check the weather and suggest what to pack. Recommend me a restaurant in K-town and calculate the ETA from Burbank airport to the restaurant.
