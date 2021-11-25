import requests
 
def edit_readme(reachble):
    orig = 'COMMIT_HISTORY'
    
    if(reachble):
      new = '<img alt="DigitalGreyHat Activity Graph" src="https://activity-graph.herokuapp.com/graph?username=DigitalGreyHat&bg_color=1F222E&color=F8D866&line=F85D7F&point=FFFFFF&hide_border=true" />'
    else:
      new = ''
    
    with open('./.readmify/readme.base.md', 'r') as f:
        text = f.readlines()
        new_text = [item.replace(orig, new) for item in text]

    with open('README.md', 'w') as f:
        for line in new_text:
           f.write(line)
 
def main():
    url = 'https://activity-graph.herokuapp.com/graph?username=DigitalGreyHat&bg_color=1F222E&color=F8D866&line=F85D7F&point=FFFFFF&hide_border=true'
    r = requests.get(url)
    if('Error' in r.text):
      edit_readme(False)
    else:
      edit_readme(True)
 
if __name__ == '__main__':
    main()