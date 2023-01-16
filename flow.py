


data = {
    "target_id": 1,
    "recon": [
            {
            "title": "OSINT",
            "active": True,
            "children": [
                {
                    "title": "Domain information",
                    "active": True,
                    "name": "domain"
                },
                {
                    "title": "Emails addresses and users",
                    "active": True,
                    "name": "email"
                },
                {
                    "title": "Password leaks",
                    "active": True,
                    "name": "password"
                },
                {
                    "title": "Metadata finder",
                    "active": True,
                    "name": "metadata"
                },
                {
                    "title": "Google Dorks",
                    "active": True,
                    "name": "google_dork"
                },
                {
                    "title": "Github Dorks",
                    "active": True,
                    "name": "github_dork"
                },
                {
                    "title": "GitHub org analysis",
                    "active": True,
                    "name": "github_org"
                }
            ]
        },
        {
            "title": "Host",
            "active": True,
            "children": [
                {
                    "title": "WhoisXML",
                    "active": False,
                    "name": "whoisxml"
                },
                {
                    "title": "IP CDN",
                    "active": True,
                    "name": "ipcdn"
                },
                {
                    "title": "Check Firewall",
                    "active": False,
                    "name": "wafw00f"
                },
                {
                    "title": "Nmap Scan",
                    "active": False,
                    "name": "nmap"
                },
                {
                    "title": "Smap Scan",
                    "active": False,
                    "name": "smap"
                },
                {
                    "title": "Search Sploit",
                    "active": False,
                    "name": "searchsploit"
                },
                {
                    "title": "BruteSpray",
                    "active": False,
                    "name": "brutespray"
                }
            ]
        },
        {
            "title": "Subdomain",
            "active": True, 
            "children": [ 

                {
                    "active": True,
                    "name": "sub_scraping"
                },
                {
                    "active": True,
                    "name": "sub_active"
                },
                {
                    "active": True,
                    "name": "sub_passive"
                },
                
                {
                    "active": True,
                    "name": "sub_crt"
                },
                {
                    "active": True,
                    "name": "sub_noerror"
                },
                {
                    "active": False,
                    "name": "sub_brute"
                },
                {
                    "active": False,
                    "name": "sub_analytics"
                },
                {
                    "active": False,
                    "name": "sub_permut"
                },
                {
                    "active": True,
                    "name": "sub_dns"
                },
                {
                    "active": False,
                    "name": "zonetransfer"
                }
            ]
        },
        {
            "title": "Web",
            "active": True,
            "children": [
                {
                    "title": "Web Prober",
                    "active": False,
                    "name": "web_probe"
                },
                {
                    "title": "Web templates",
                    "active": True,
                    "name": "web_template"
                },
                {
                    "title": "CMS Scanner",
                    "active": False,
                    "name": "cms_scanner"
                },
                {
                    "title": "Url extraction",
                    "active": False,
                    "name": "url_extraction"
                },
                {
                    "title": "URL patterns Search and filtering",
                    "active": False,
                    "name": "url_filter"
                },
                {
                    "title": "Favicon Real IP",
                    "active": False,
                    "name": "fav_ip"
                },
                {
                    "title": "Javascript analysis",
                    "active": False,
                    "name": "js_analysis"
                },
                {
                    "title": "Fuzzing",
                    "active": False,
                    "name": "fuzzing"
                },
                {
                    "title": "URL sorting by extension",
                    "active": False,
                    "name": "url_sorting"
                },
                {
                    "title": "Wordlist generation",
                    "active": False,
                    "name": "wordlist_generation"
                },
                {
                    "title": "Passwords dictionary creation ",
                    "active": False,
                    "name": "password_dictionary"
                },
                {
                    "title": "Web Probe Simple",
                    "active": True,
                    "name": "webprobe_simple"
                }
            ]
        }
    ]
}
requirement = {
"zonetransfer": None,
"sub_passive": None,
"sub_crt": None,
"sub_active": ("sub_passive", "sub_crt",),
"sub_noerror": None,
"sub_brute": None,
"sub_dns": ("sub_active", "sub_noerror"),
"sub_scraping": ("sub_dns",),
"sub_analytics": ("sub_scraping",),
"webprobe_simple":("sub_analytics",),
"webprobe_full": ("webprobe_simple",),
"subtakeover": ("webprobe_full"),
"s3buckets": ("sub_analytics"),
"cdnprovider": ("sub_dns"),
"portscan": ("sub_dns"),
"waf_checks": ("webprobe_full"),
"nuclei_check": ("webprobe_full"),
"fuzz": ("webprobe_full"),
"jschecks": ("urlchecks"),
"cms_scanner": ("webprobe_full"),
"url_gf": ("urlchecks"),
"wordlist_gen": ("url_gf"),
"password_dict": None,
"url_ext": ("urlchecks"),

}



data = data["recon"]
def check_active(data_to_check, keyword_check):
    for item in data_to_check:
        for i in item["children"]:
            if i["active"] and i["name"] == keyword_check and item["active"] == True:
                return True
            elif not i["active"] and i["name"]==keyword_check and item["active"] == True:
                print(f"requirement for {keyword_check} missing ❌")
                return False

def validate_requirement(data_to_check, action, requirement):
    if check_active(data_to_check, action):
        new_action = requirement.get(action)
        if new_action == None:
            # print(f"Requiment for {action} fullfiled!!! ✅")
            return 0
        else:
            for a in new_action:
                validate_requirement(data_to_check, a, requirement)
                return a
    else:
        return 1

for i in requirement.keys():
    result = validate_requirement(data, i, requirement)
    print(result)


def requirement_checking(requirement, task_result, key):
    arr = requirement[key]
    for i in arr: 
        if task_result(i)["status"] == "fail":
            return False
    return True
    
def Q_task():
    pass
