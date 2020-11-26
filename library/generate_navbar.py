navbar = [
    {
        "id": "home",
        "name": "Home",
        "url": "/"
    },
    {
        "id": "books",
        "name": "Books",
        "url": "/books",
        "submenu": [
            {
                "id": "book_search",
                "name": "Search",
                "url": "/book/search"
            }
        ]
    },
    {
        "id": "authors",
        "name": "Authors",
        "url": "/authors",
        "submenu": [
            {
                "id": "author_search",
                "name": "Search",
                "url": "/authors/search"
            }
        ]
    }
]

def load_menu_item():
    text = ""
    with open("library/components/menu_item.html") as f:
        text = f.read()
    return text

def load_navmenu():
    text = ""
    with open("library/components/navmenu.html") as f:
        text = f.read()
    return text

menu_item = load_menu_item()
nav_menu = load_navmenu()

def generate_navbar(active_element):
    count = 1
    menu = ""
    for item in navbar:
        submenu = ""
        if "submenu" in item.keys():

            sub_url = item["submenu"][0]["url"]
            sub_name = item["submenu"][0]["name"]
            if active_element == item["submenu"][0]["id"]:
                submenu = submenu + '<ul class="sub-menu">' + menu_item.format(count=count, url=sub_url, name=sub_name, active="fusion-dropdown-submenu current-menu-item page_item current_page_item", submenu="", style='') + '</ul>' + "\n"
            else:
                submenu = submenu + '<ul class="sub-menu">' + menu_item.format(count=count, active="fusion-dropdown-submenu", url=sub_url, name=sub_name, submenu="", style='') + '</ul>' "\n"
        
        url = item["url"]
        name = item["name"]
        if active_element == item["id"]:
            menu = menu + menu_item.format(count=count, url=url, name=name, active="current-menu-item page_item current_page_item", submenu=submenu, style='style="height: 86px;"') + "\n"
        else:
            menu = menu + menu_item.format(count=count, active="", url=url, name=name, submenu=submenu, style='style="height: 86px;"') + "\n"
        count += 1
    return nav_menu.format(menu=menu)
