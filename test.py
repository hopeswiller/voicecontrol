triggers = ["hey hopes"]


if any(x in triggers for x in ["hey", "yo"]):
    print("true")


import geocoder

g = geocoder.ip("me")
print(g[0],g.city, g.lng)

# import ipinfo

# access_token = "014971cac59438"
# handler = ipinfo.getHandlerAsync(
#     access_token, cache_options={"ttl": 30, "maxsize": 128}
# )

# async def do_req():
#     details = await handler.getDetails()
#     print(details.city)
#     print(details.loc)


# import asyncio

# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_req())
