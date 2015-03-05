import StringIO
import csv

from tornado import template
loader = template.Loader(".")
speakers = [("""./headshots/Gavin.png""",
"""Gavin Andresen""",
"""Core Developer, Bitcoin""",
"""Gavin is the Chief Scientist at the Bitcoin Foundation and is one of the longest serving and most widely respected developers of the Bitcoin protocol. Prior to this, he wrote 3D graphics software in Silicon Valley."""),
("""./headshots/Charlie.png""",
"""Charlie Lee""",
"""Creator, Litecoin""",
"""Charlie is the creator of Litecoin, the most popular alternative to Bitcoin. He is currently at Coinbase leading the product engineering team. Prior to that, he spent 6 years at Google. Charlie is also an MIT alum."""),
("""./headshots/Adam.png""",
"""Adam Ludwin""",
"""Founder, Chain""",
"""Adam is a founder of Chain, a way for developers to fully take advantage of the security and power of the bitcoin ecosystem by abstracting away the superfluous details of the blockchain."""),
("""./headshots/Jeremy.png""",
"""Jeremy Allaire""",
"""CEO, Circle""",
"""Jeremy is the CEO and cofounder of Circle Internet Financial and Chairman at Brightcove, which he also founded. His roles prior to Circle include CEO of Brightcove and CTO of Macromedia."""),
("""./headshots/Juthica.png""",
"""Juthica Chou""",
"""President, LedgerX""",
"""Juthica is the current cofounder and president of LedgerX. Prior to her current role, she specialized in algorithmic trading at Goldman Sachs for 7 years as a derivatives trader. Juthica is also an MIT alum."""),
("""./headshots/Peter.png""",
"""Peter Todd""",
"""Core Developer, Bitcoin""",
"""Peter is currently working on prooftrains and treechains, with permissionless development, decentralized mining, and scalability. He also consults for Dark Wallet and MasterCoin."""),
("""./headshots/Andreas.png""",
"""Andreas Antonopoulos""",
"""Author, Mastering Bitcoin""",
"""Andreas Antonopoulos is a technologist and serial entrepreneur who has become one of the most prominent figures in bitcoin. He is also a widely published author of articles and blog posts on bitcoin."""),
("""./headshots/Joi.png""",
"""Joi Ito""",
"""Director, MIT Media Lab""",
"""Joi has been recognized for his work as an activist, entrepreneur, and VC. As director of the MIT Media Lab, he explores how radical approaches to science and technology can transform society in substantial ways."""),
("""./headshots/Joshua.png""",
"""Joshua Lim""",
"""Treasury & Trading, Circle""",
"""Joshua is the current head of treasury and trading operations at Circle. Prior to that, he worked as an associate at Goldman Sachs for five years as a trader specializing in exotic derivatives. Joshua is an MIT alum."""),
("""./headshots/Matt.png""",
"""Matt Corallo""",
"""Cofounder, Blockstream""",
"""Matt has been working on pioneering sidechain and Bitcoin extensibility technology since its inception. He has actively contributed to Bitcoin Core and its testing infrastructure, and to BitcoinJ."""),
("""./headshots/Constance.png""",
"""Constance Choi""",
"""Principal, Seven Advisory""",
"""Constance specializes in bridging the gap between tech companies and complex regulatory frameworks. Prior to Seven she worked as Chief Compliance Officer at Kraken Exchange."""),
("""./headshots/Robert.png""",
"""Bobby Cho""",
"""Director, itBit""",
"""Bobby currently serves as Director of Business Development at itBit. Previously, Bobby was Vice President of Trading at SecondMarket specializing in trading bitcoin and illiquid asset-backed securities."""),
("""./headshots/Melanie.png""",
"""Melanie Shapiro""",
"""CEO, CryptoLabs""",
"""Melanie is the founder of Case, a multi-sig hardware bitcoin wallet that is GSM-enabled and credit card-size. Prior to this, she received a PhD in Consumer Behavior and co-founded the instant messaging company, Digsby."""),
("""./headshots/Arvind.png""",
"""Arvind Narayanan""",
"""Professor, Princeton""",
"""Arvind is currently an assistant professor at Princeton, where his major research areas are web privacy, big data, and bitcoin and other cryptocurrencies. He is most known for his research in data privacy."""),
("""./headshots/Alan.png""",
"""Alan Reiner""",
"""CEO, Armory""",
"""Alan is the core developer for Armory, a company focused on providing enterprise Bitcoin security solutions. He first came on to the bitcoin scene as a miner, he now develops the Armory Bitcoin Client, one of the first wallets to make cold storage and multisig accessible through a user interface."""),
("""./headshots/Andy.png""",
"""Andy Ofiesh""",
"""Developer, Armory""",
"""Andy is currently one of the lead developers at Armory Technologies. He has masters degrees in software engineering and computer science, and is also a standup comic in Boston."""),
("""./headshots/Jerry.png""",
"""Jerry Brito""",
"""Executive Director, Coin Center""",
"""Jerry Brito is executive director of Coin Center, a nonprofit research and advocacy center focused on the public policy issues facing cryptocurrency technologies such as Bitcoin."""),
("""./headshots/Elaine.png""",
"""Elaine Shi""",
"""Professor, UMD""",
"""Elaine Shi is an assistant professor of computer science at the University of Maryland and a member of the Maryland Cybersecurity Center. Her research generally focuses on security, privacy, and applied cryptography."""),
("""./headshots/Andrew.png""",
"""Andrew Miller""",
"""Grad. Student, UMD""",
"""Andrew is a computer science PhD student at the University of Maryland, in the Cybersecurity Center (MC2) and programming language lab (PLUM). He studes distributed systems, programming languages, and cryptography. He is especially interested in secure p2p networks, such as Bitcoin."""),
("""./headshots/Christian.png""",
"""Christian Catalini""",
"""Professor, MIT Sloan""",
"""Christian is currently a professor at MIT Sloan where he focuses the brunt of his research on the economics of innovation, entrepreneurship and scientific productivity. He is one of the lead researchers on the MIT Bitcoin Project."""),
("""./headshots/Elizabeth.png""",
"""Elizabeth Stark""",
"""EIR, StartX""",
"""Elizabeth is currently an entrepreneur in residence, fellow at Coin Center, and the EIR at StartX. As a graduate of Harvard law, she has been teaching about and leading the charge on policy issues in tech."""),
("""./headshots/Eric.png""",
"""Eric Martindale""",
"""Developer Evangelist, BitPay""",
"""Eric acts as BitPay's chief developer evangelist and open source advocate, and was the founding engineer and CTO of several companies related to decentralization.  He is the co-host of the DECENTRALIZE podcast, and a proud autodidact and polymath."""),
("""./headshots/Harry.png""",
"""Harry Yeh""",
"""Managing Partner, Binary Financial""",
"""Harry is a Managing Partner at Binary Financial and is known in the digital currency space for trading and facilitating large block trades for high net worth clients and institutions. Harry is a Serial Entrepreneur with a software and infrastructure engineering background, and has over 15 years experience in the Technology and Business Field."""),
("""./headshots/Kristov.png""",
"""Kristov Atlas""",
"""Security Engineer, Blockchain""",
"""Kristov Atlas is currently a Security Engineer at Blockchain. Prior to joining the Blockchain team, he was an independent security researcher and application security consultant. Kristov has been focused on Bitcoin application security since early 2013."""),
("""./headshots/Will.png""",
"""Will O'Brien""",
"""CEO, BitGo""",
"""Will O'Brien: Will is CEO and co-founder of BitGo, the leading bitcoin security platform and a pioneer in multi-sig technologies. He previously held leadership roles at Big Fish Games, TrialPay, Random Walk Computing, and founded startups in consumer internet and media. Will holds an MBA from MIT Sloan and a B.A. in Computer Science from Harvard."""),
("""./headshots/Ryan.png""",
"""Ryan Selkis""",
"""Director, Digital Currency Group""",
"""Ryan Selkis is Director of Investments at Digital Currency Group, which builds, incubates and seeds digital currency and blockchain technology ventures. Ryan was also recognized in 2014 as "Bitcoin's Most Insightful Journalist" for his industry-leading blog, the "Two-Bit Idiot's Daily Bit." """),
("""./headshots/Ben.png""",
"""Ben Chan""",
"""Engineer, BitGo""",
"""Ben leads the developer platform at BitGo and works on the APIs and SDKs to make it easy to integrate secure Multi-sig wallets. He was introduced to Bitcoin in 2012 and grew to be a huge believer in blockchain technology, especially in the areas of P2SH, contracts and multisig oracles. """),
("""./headshots/Madars.png""",
"""Madars Virza""",
"""Developer, Zerocash""",
"""Madars is currently a graduate student at MIT CSAIL under Ronald Rivest. He obtained his B.Sc from University of Latvia. He is also working on Zerocash, a decentralized anonymous payment system for Bitcoin."""),
("""./headshots/Joe.png""",
"""Joe Zhou""",
"""CEO, Alt-Options LLC""",
"""Joe is the founder and current CEO of Alt-Options LLC, a Boston based Bitcoin derivates exchange. He has had experience in the investment banking, private M&A and institutional FX trading space as well as over 6 years of experience trading equities/derivatives"""),
("""./headshots/Marco.png""",
"""Marco Cuesta""",
"""Vice President of Sales, Alt-Options LLC""",
"""Marco is the cofounder and Vice President of Sales of Alt-Options LLC, a Boston based Bitcoin derivates exchange. He founded the Boston University Bitcoin Club, has over 5 years of securities trading experience, and entrepreneurial sprit that expands a variety sectors."""),
("""./headshots/Shea.png""",
"""Ryan Shea""",
"""CEO, Onename""",
"""Ryan is the Co-founder and CEO of Onename, which gives users a digital passport to login around the web and stay in control of their identity and data. He co-founded HackPrinceton, was on the Forbes 30 Under 30 for Consumer Tech, and is passionate about open source and decentralization."""),
("""./headshots/Weiss.png""",
"""Matt Weiss""",
"""Portfolio Director, IDEO Futures""",
"""Matt is a Portfolio Director at IDEO's Cambridge Studio, with 14 years of experience as a financial services entrepreneur. This summer, he's leading IDEO Futures _Lab on Bitcoin and Blockchain. Matt is an MIT alum. """),
("""./headshots/Gerber.png""",
"""Joe Gerber""",
"""Director, IDEO Futures""",
"""Joe helps lead IDEO Futures, a team dedicated to creating the new ventures on that explore the edge of technology and human-centered design. Joe is an MIT alum. """),
("""./headshots/Dan.png""",
"""Dan Elitzer""",
"""MIT Bitcoin Project""",
"""Dan founded the MIT Bitcoin Club and is a second year MBA Candidate at MIT Sloan. Prior to attending MIT, Dan worked at Grameen Foundation, where he became interested in Bitcoin."""),
("""./headshots/Sam.png""",
"""Sam Udotong""",
"""Founder, Fireflies""",
"""Sam is a junior at MIT studying aerospace engineering. He participated in the summer-long MIT BitComp and his app Fireflies (an on-demand p2p delivery platform) won the Awesome award."""),
("""./headshots/Jonathan.png""",
"""Jonathan Harvey-Buschel""",
"""President, MIT Bitcoin Club""",
"""Jonathan is the current president of the MIT Bitcoin Club, and a freshman studying EE at MIT. He entered the world of cryptocurrency via dogecoin mining, and is currently working on BitVend, a vending machine platform that accepts Bitcoin."""),
("""./headshots/Gardner.png""",
"""Jeremy Gardner""",
"""Founder, College Cryptocurrency Network""",
"""Jeremy attended both Bard College and University of Michigan, where he developed a multidisciplinary study in political strategy. While at Michigan, he founded the CCN, an international nonprofit organization. He also runs business and operations for Augur, the world's first decentralized prediction market software."""),
("""./headshots/Rubin.png""",
"""Jeremy Rubin""",
"""MIT Bitcoin Project""",
"""Jeremy is an EECS junior at MIT. He came onto the bitcoin scene with Tidbit, a system to replace web ads with cryptocurrency mining (currently fighting NJ). Jeremy is also a founder of the MIT Bitcoin Project."""),
("""./headshots/Jinglan.png""",
"""Jinglan Wang""",
"""President, Wellesley Bitcoin""",
"""Jing is currently a junior at Wellesley College, studying studio art and CS. She is working on developing a cryptocurrency course at Wellesley. She also writes and illustrates comics on Bitcoin and cryptography.""")]
scsv= open("day1.csv", "r").read()
day1= []
for row in csv.reader(scsv.split('\n'), delimiter=','):
	talkers = ", ".join([x for x in row[2:] if x != ""])
	day1.append([row[0],row[1],talkers])

scsv= open("day2.csv", "r").read()
day2= []
for row in csv.reader(scsv.split('\n'), delimiter=','):
	talkers = ", ".join([x for x in row[2:] if x != ""])
	day2.append([row[0],row[1],talkers])

goldsponsors = [("""./sponsors/chain.png""","Chain"),("""./sponsors/digitalbtc.png""","DigitalBTC")]
silversponsors = [("""./sponsors/circle.png""","Circle"),("""./sponsors/fidelity.png""","Fidelity")]
mediasponsors = [("""./sponsors/btcfoundation.png""","Bitcoin Foundation"),("""./sponsors/ccn.png""","College Cryptocurrency Network")]
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1=day1,day2=day2,goldsponsors=goldsponsors,silversponsors=silversponsors,mediasponsors=mediasponsors))
