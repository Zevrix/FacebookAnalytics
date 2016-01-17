#creates a txt database of my facebook messages

import urllib.request
response = urllib.request.urlopen('file:///C:/Python33/messages.htm') #change location
html = response.read()
html = str(html)

messages = []

while True:
    start = html.index('<div class="message_header"><span class="user">')
    html = html[start:]
    end = html.index('</p><div class="message">')
    text = html[47:end]
    start2 = text.index('</span><span class="meta">')
    end2 = text.index('</span></div></div><p>')
    name = text[:start2]
    if len(name) > 20:
        name = name[:20]
    elif len(name) < 20:
        name = name + ' '*(20-len(name))
    print(name,'|',text[start2+26:end2],'|',text[end2+22:])
    with open("FacebookMessages.txt", "a") as text_file:
        print(name,'|',text[start2+26:end2],'|',text[end2+22:],file = text_file)
    messages.append([name,text[start2+26:end2],text[end2+22:]])
    html = html[end+10:]

#January 1, 2012 (account creation)
#Friday, October 16th, 2015 late at night (download date)
