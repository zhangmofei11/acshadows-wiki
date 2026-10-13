import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/c78b78fd4ca4923c090e9c0181cf7709"></script>
<script data-cfasync="false" src="https://bauval.org/14/7d5099523b6195236264445b2f1be920"></script>
<script>
  atOptions = {
    'key' : 'b4352f63a35aaeb5557c7fe1b8afaae4',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/b4352f63a35aaeb5557c7fe1b8afaae4"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-c78b78fd4ca4923c090e9c0181cf7709"></div>
</div>'''

files = ['index.html', 'characters.html', 'missions.html', 'weapons.html', 'skills.html', 'collectibles.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'b4352f63a35aaeb5557c7fe1b8afaae4' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-c78b78fd4ca4923c090e9c0181cf7709' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
