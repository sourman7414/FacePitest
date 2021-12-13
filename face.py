import fire , json

class Facepi:
    def readConfig(self):
        with open('Config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    
    def self(self):
        print(self.readConfig())
        config = self.readConfig()
        print(config['api_key'])
    
    def writeconfig(self,config):
        with open('Config.json','w', encoding='utf-8') as f:
            json.dump(config,f)

    def setconfig(self):
        config = self.readConfig()
        print("不更改config請按enter鍵")
        api_key = input(f"輸入更改的api_key[{config['api_key']}]: ")
        if api_key:  config['api_key'] = api_key
        title = input(f"輸入更改的title[{config['title']}]: ")
        if title: config['title'] = title 
        self.writeconfig(config)
    
    #use online image
    def detectImageUrl(self,imageurl):
        headers={
            #request headers
            'Content - Type': 'application/json',
            'Ocp-Apim-Subscripition-key': self.readConfig()['api_key'],
        }
        params=urllib.parse.urlencode({
            # request parameters
            'returnFaceId':'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender',
            #'recognitionModel': 'recognition_04',
            d
            })


            #
        }


if __name__=="__main__":
    fire.Fire(Facepi)



