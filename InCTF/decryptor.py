import base64

mkey="UXpwY1VIbDBhRzl1TWpkY08wTTZYRkI1ZEdodmJqSTNYRk5qY21sd2RITTdRenBjVjJsdVpHOTNjMXh6ZVhOMFpXMHpNanRET2x4WAphVzVrYjNkek8wTTZYRmRwYm1SdmQzTmNVM2x6ZEdWdE16SmNWMkpsYlR0RE9seFhhVzVrYjNkelhGTjVjM1JsYlRNeVhGZHBibVJ2CmQzTlFiM2RsY2xOb1pXeHNYSFl4TGpCY08wTTZYRkJ5YjJkeVlXMGdSbWxzWlhNZ0tIZzROaWxjVG0xaGNDNURUMDA3TGtWWVJUc3UKUWtGVU95NURUVVE3TGxaQ1V6c3VWa0pGT3k1S1V6c3VTbE5GT3k1WFUwWTdMbGRUU0RzdVRWTkQK"
msg="PXgRVzcRMWkNZGIccglMH3QwUAR5XxgQdDh6PHJFaVJ6KkQCRAVqGHMfKyB8GEUQOlcRF0RTcj90MUR8RSUnE3gZOhIHM1A7bzFuCW0qSFN6IkgEKD9eKz0pEytBCHIpdFNYU3cKFRF4CSYTOg9uAkUFGBR0IHo/ciY3DnceWToCGXEBdANuZW1EWAV6N0QcATwfRTsEKCNtNFA4PBV8QzosXwdFEkgadjEzC3cZJgIDGEgSdBl2XW16Lwp3HzonAyJIGHoDJxBMJSJbJRlxKXQcZl1tX3I4PEtWPApYFixFF248cw0JTXo0GCo/RBgodDl6bXJaan48E2QYDT8KLG0LRCBCHB0DeR8AJzxEVDR6MTc2TzILCT5nUVgPZylkIXVyIW03YR10IFQ4dzlqMkNfdS51eVQkdjoZWG49cjx2HSBKejQIADJUdlJDUnYhQVVQaXR4Dkh9QiZXAFZ2J0IgFSR0QUtUdzJ1PDItSj4SJjEwdVZyFkQ3cjB0IDQy"
#a=base64.b64decode(_mkey)
b=base64.b64decode(msg)

def master_xor(msg,mkey):
    l = len(mkey)
    xor_complete = ""

    for i in range(0, len(msg)):
        xor_complete += chr(ord(msg[i]) ^ ord(mkey[i%l]))
    
    return xor_complete

print(master_xor(b,mkey))