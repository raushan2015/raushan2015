<!-- ===================== HEADER ===================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Raushan%20Kumar%20Chaudhary&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Server%20%26%20Infrastructure%20%7C%20Full-Stack%20Developer%20%7C%20Home%20Labber&descAlignY=58&descSize=16" alt="header" />
</p>

<p align="center">
  <a href="https://www.raushan7.com.np">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=640&lines=%F0%9F%8C%8F+From+Nepal+%E2%86%92+Qatar+%E2%86%92+Japan;%F0%9F%8F%A0+I+run+my+own+home+lab+data+center;%F0%9F%90%B3+Linux+%E2%80%A2+Docker+%E2%80%A2+Nginx+%E2%80%A2+DNS+%E2%80%A2+VPN;%F0%9F%9B%A0%EF%B8%8F+Building+TECHSHAN-IMS+end-to-end;%F0%9F%94%8D+Debug+step+by+step%2C+never+by+guesswork" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://www.raushan7.com.np"><img src="https://img.shields.io/badge/Portfolio-raushan7.com.np-0ea5e9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
  <a href="mailto:mail@raushan7.com.np"><img src="https://img.shields.io/badge/Email-mail%40raushan7.com.np-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Based%20in-Japan%20🇯🇵-bc002d?style=for-the-badge" alt="Japan" />
</p>

---

## 👋 About Me

I'm **Raushan**, originally from **Nepal** 🇳🇵 and now living in **Japan** 🇯🇵. I study **Information Systems** at Global Information Career Academy (グローバル情報キャリア学院). I work on two things: **servers and networks**, and **full-stack software** that runs on them.

Before coming to Japan, I spent **3 years in Qatar** 🇶🇦 doing data entry for an engineering-maintenance company. Two things from that job stayed with me:

- 📉 When the network or an internal system went down, **all the work on site stopped with it.** That's why I want to build and look after infrastructure.
- 📝 A lot of time went into **copying and checking inventory and sales data by hand.** That's why I build software that removes that kind of work.

> 💡 **My strength:** I don't guess when something breaks. I isolate the problem layer by layer (process → port → DNS → router → ISP), fix it, write down what happened, and automate the fix so it doesn't happen again.

---

## 🏠 Home Labber at Heart

I run a **home lab** 🖥️ as my own small data center. It hosts a bunch of **self-hosted services I use every day**. I built it, and I also run and monitor it by myself.

<table>
<tr>
<td width="50%" valign="top">

**🧱 What I run**
- 🐳 **Docker** containers on **Linux**
- 🌐 **Nginx** reverse proxy with **SSL/TLS**
- 🛡️ **Pi-hole** for network-wide ad blocking and local DNS
- 🎬 **Plex** as my media server
- 🗄️ **PostgreSQL · Redis · MinIO** for my own apps
- 📦 **TECHSHAN-IMS**, running in production on my own hardware

</td>
<td width="50%" valign="top">

**⚙️ How I run it**
- 🔌 Router port forwarding and **DNS** name resolution
- 🔥 **Firewall** access control and **VPN** remote access
- 📊 Monitoring and log-based troubleshooting (`ping`, `traceroute`, `dig`, logs)
- 🤖 Automated **backups and deployments** (shell scripts + CI/CD)
- 🧪 Changes go to **staging → production**
- 📚 Every setup and fix is **documented**

</td>
</tr>
</table>

```mermaid
flowchart LR
    U([🌍 Internet]) --> CF[☁️ Cloudflare DNS]
    CF --> R[📶 Router<br/>Port-forward + Firewall]
    V([🔐 VPN client]) --> R
    R --> H[🐧 Linux host]
    subgraph Docker["🐳 Docker"]
        N[🌐 Nginx<br/>Reverse proxy + SSL]
        N --> IMS[📦 TECHSHAN-IMS]
        N --> PLEX[🎬 Plex]
        IMS --> DB[(🐘 PostgreSQL)]
        IMS --> RD[(⚡ Redis)]
        IMS --> S3[(🪣 MinIO)]
        PH[🛡️ Pi-hole DNS]
    end
    H --> N
    H --> PH
```

---

## 🚀 Featured Project: TECHSHAN-IMS

An **inventory management system** that I design, build, and run by myself. It's my fix for the manual data work I did in Qatar.

| Layer | Tech |
|---|---|
| 🎨 Frontend | Next.js · React |
| ⚙️ Backend | Node.js · Express · TypeScript |
| 🗄️ Data | PostgreSQL · Redis · MinIO |
| 🖥️ Desktop | Electron + SQLite, **works offline and syncs automatically when the connection comes back** |
| 🚢 Ops | Docker · Nginx · home lab hosting · GitHub branch workflow · staging → production |

**Features:** authentication, sales, purchasing, reports and business documents, and database design built from scratch.

🤖 I use **AI coding tools** to move fast, but I don't ship code I haven't checked. I read what they produce, check it against the official docs, and test it before it goes in.

---

## 💻 Tech Stack

**☁️ Infrastructure & DevOps**
<p>
  <img src="https://skillicons.dev/icons?i=linux,docker,nginx,cloudflare,bash,powershell,githubactions,git,github&perline=9" alt="infra" />
</p>
<p>
  <img src="https://img.shields.io/badge/Pi--hole-96060C?style=flat-square&logo=pi-hole&logoColor=white" />
  <img src="https://img.shields.io/badge/Plex-E5A00D?style=flat-square&logo=plex&logoColor=white" />
  <img src="https://img.shields.io/badge/MinIO-C72E49?style=flat-square&logo=minio&logoColor=white" />
  <img src="https://img.shields.io/badge/Linode-00A95C?style=flat-square&logo=linode&logoColor=white" />
  <img src="https://img.shields.io/badge/VPN-4B5563?style=flat-square&logo=wireguard&logoColor=white" />
  <img src="https://img.shields.io/badge/DNS%20%7C%20Firewall%20%7C%20SSL-1f2937?style=flat-square" />
</p>

**🧑‍💻 Development**
<p>
  <img src="https://skillicons.dev/icons?i=ts,js,nodejs,express,nextjs,react,electron,tailwind,html,css,python,java&perline=12" alt="dev" />
</p>

**🗄️ Databases**
<p>
  <img src="https://skillicons.dev/icons?i=postgres,redis,sqlite" alt="db" />
</p>

---

## 🎓 Education & Certifications

| | |
|---|---|
| 🏫 **Global Information Career Academy** (Japan) | Information Systems · 2025 – present |
| 🗾 **Tokyo Management College – Global Study Center** (Japan) | Japanese language · 2023 – 2025 |
| 📘 **Reliance International Academy** (Nepal) | +2 (Higher Secondary) · 2016 – 2018 |
| 🏅 **TOEIC 835** | 2024 |
| 🇯🇵 **JLPT N3** | 2024 |

**🗣️ Languages:** English (TOEIC 835) · Japanese (JLPT N3) · Nepali

---

## 🎯 What I'm Looking For

- 🔧 **Network and infrastructure roles:** building and running servers and networks, with the goal of moving into **cloud infrastructure design**
- 🤝 Working on projects in **server infrastructure, self-hosting and scalable backends**
- 🌱 Currently learning: advanced Linux administration, container orchestration, networking, and cloud architecture

**Outside tech:** 📖 reading · 🏃 running · 🎬 movies

---

## 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=raushan2015&show_icons=true&theme=tokyonight&hide_border=true" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=raushan2015&layout=compact&theme=tokyonight&hide_border=true" alt="top langs" />
</p>
<p align="center">
  <img src="https://nirzak-streak-stats.vercel.app/?user=raushan2015&theme=tokyonight&hide_border=true" alt="streak" />
</p>

---

<p align="center">
  <a href="https://facebook.com/raushanchy7"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" /></a>
  <a href="https://instagram.com/raushan.2015"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
  <a href="https://paypal.me/raushan2015"><img src="https://img.shields.io/badge/Support%20me-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" /></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=110&section=footer" alt="footer" />
</p>
