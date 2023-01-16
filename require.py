
def requirement(required_action, Object, Array):
    if Object.get(required_action, None) == None:
        Array.append(required_action)
        return 0    
    else:
        next_action = Object.get(required_action, None)
        s = requirement(next_action, Object, Array)
        Array.append(required_action)
        return s

def concurrency_level(required_action, Object):
    if Object.get(required_action, None) == None:
        return 0
    else: 
        next_action = Object.get(required_action, None)
        s = concurrency_level(next_action, Object) + 1
        return s


web_flow = {
            "web_probe": None,
            "web_template": "web_probe",
            "cms_scanner": "web_probe",
            "url_extraction": "web_probe",
            "url_filter": "url_extraction",
            "fav_ip": None,
            "js_analysis": "url_extraction",
            "fuzzing": "web_probe",
            "url_sorting": "url_extraction",
            "wordlist_generation": "js_analysis",
            "password_dictionary": None,
        }

requirement("js_analysis", web_flow, js_analysis)
requirement("wordlist_generation", web_flow, wordlist_generation)
requirement("fuzzing", web_flow, fuzzing)
requirement("fav_ip", web_flow, fav_ip)


d = web_flow
r = {}
arr = list(d.keys())
for t,i in enumerate(arr):
    k = d[i]
    r[k] = []
    r[k].append(i)
    for j in arr:
        if k == d[j] and j!= i:
            r[k].append(j)



class Q_Handler():
    def __init__(self, data):
        self._data=data
        self.conc = {}
    def run(self, action=None):
        if action in self._data.keys():
            for i in self._data[action]:
                async_task(i, hook=self.tranduce)
                self.conc[i] = "added to Q"
    def tranduce(self, task):
        action = task
        print(f"this task run after {action}")
        self.run(action)
    def check(self):
        return self.conc
print(r)
q = Q_Handler(r)
q.run()
print(q.check())