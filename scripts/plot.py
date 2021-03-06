import matplotlib.pyplot as plt
import matplotlib as mpl
from labellines import labelLines
from yaml import safe_load


def bar(gwaff):
    with open("config.yml", "r") as file:
        config = safe_load(file)

    if config["darkmode"]:
        plt.style.use("dark_background")

    users = {}
    for user in gwaff:
        try:
            users[
                abs(
                    gwaff[user]["total_xp"][list(gwaff[user]["total_xp"])[-1]]
                    - gwaff[user]["total_xp"][list(gwaff[user]["total_xp"])[-2]]
                )
            ] = gwaff[user]["name"]
        except IndexError:
            break

    users = sorted(users.items(), reverse=True)

    y = []
    x = []
    for user in users[0 : int(config["bar"]["range"])]:
        y.append(user[0])
        x.append(user[1].split("#")[0])

    plt.figure(figsize=(14, 7))

    plt.bar([i for i, _ in enumerate(x)], y)
    plt.xticks([i for i, _ in enumerate(x)], x, rotation="vertical")
    plt.title(f"{config['title']}\ntop xp gains for the past 2 days")
    plt.xlabel(f"{config['bottom_message']}")
    plt.ylabel(f"xp gained")
    plt.show()


def line(gwaff):
    with open("config.yml", "r") as file:
        config = safe_load(file)

    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(
        color=[
            "blue",
            "green",
            "red",
            "cyan",
            "magenta",
            "yellow",
            "black",
            "purple",
            "pink",
            "brown",
            "orange",
            "teal",
            "coral",
            "lightblue",
            "lime",
            "lavender",
            "turquoise",
            "darkgreen",
            "tan",
            "salmon",
            "gold",
        ]
    )
    if config["darkmode"]:
        plt.style.use("dark_background")
    plt.figure(figsize=(14, 7))
    g = 0
    q = 0
    rankrange = [0, config["plot"]["rank_range"]]
    for user in gwaff:
        if g < config["plot"]["range"]:
            if q < config["plot"]["range"] - 1:
                y = [0]
                x = []
                total_xp = gwaff[user]["total_xp"]
                for i in zip(list(total_xp), list(total_xp)[1:]):
                    first = i[0]
                    second = i[1]
                    y.append(abs(total_xp[first] - total_xp[second]))
                if y[-1] < config["plot"]["minium_xp"]:
                    q += 1
                    g += 1
                    continue
                f = 0
                while f < len(total_xp):
                    x.append(f)
                    f += 1
                plt.plot(x, y, label=gwaff[user]["name"].split("#")[0])
                q += 1
                g += 1
            else:
                labelLines(plt.gca().get_lines(), align=True)
                plt.legend(bbox_to_anchor=(1, 1))
                plt.xlabel(
                    f"days since {list(gwaff['408355239108935681']['message_count'].keys())[0].split(' ')[0]}{config['bottom_message']}"
                )
                plt.ylabel("gain")
                title = f"{config['title']}\nrank: {rankrange[0]}-{rankrange[1]}"
                rankrange[0] = rankrange[1]
                rankrange[1] = rankrange[1] + config["plot"]["rank_range"]
                if config["plot"]["minium_xp"] > 0:
                    title += f"\ngain atleast {config['plot']['minium_xp']} to appear"
                plt.title(f"{title}\nxp gained overtime")
                plt.show()
                plt.close()

                plt.figure(figsize=(14, 7))
                q = 0
        else:
            break
