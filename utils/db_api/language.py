def language(lang,item):
    with open(f"Languages/{lang}",'r',encoding="utf8") as f:
        lang = f.read()
        item1=lang.find(item)
        if item1!=-1:
            lang = lang[item1:]
            start=lang.find('=')
            end = lang.find('\n')
            print(lang[start+2:end+1].replace("<br>","\n"))
            return lang[start+2:end+1].replace("<br>","\n")
        else:
            return item
        
def languages(lang):
    with open(f"Languages/{lang}",'r',encoding="utf8") as f:
        f = f.readlines()
        out = str()
        for i in f:
            if i[0] != '#' and  i != f[0]:
                find = i.find('=')
                i = i.replace("\n","")
                out += (f'("{i[:find-1]}","{i[find+2:]}"),')
        if out[-1] == ',':return out[:-1]
        else: return out