<a href="https://www.raushan7.com.np">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg">
    <img alt="Raushan Kumar Chaudhary: infrastructure engineer and full-stack developer in Japan. Runs a home lab on Linux, Docker and Nginx, and builds TECHSHAN and TECHSHAN-IMS." src="light_mode.svg">
  </picture>
</a>

## Projects

### 🖥️ [TECHSHAN](https://techshan.app) · server management software

A panel for your own Linux server: manage almost everything on it from the browser instead of over SSH, or ask the built-in AI assistant to do it. It runs on your machine, and your data stays there.

| | |
|---|---|
| **Server** | Dashboard, Docker, KVM virtual machines with a browser console, files and SMB shares, storage pools, network, firewall, users, backups and a terminal |
| **AI** | AI Chat that runs commands on the server and asks before changing anything, the same from Telegram, one-click install of coding agents, shared skills |
| **Install** | One command, no Docker needed: `curl -fsSL https://techshan.app/install.sh \| sudo sh` |
| **Stack** | TypeScript · NestJS · Next.js · PostgreSQL · Redis · BullMQ · pnpm + Turborepo monorepo |

🔗 [techshan.app](https://techshan.app) · [github.com/raushan2015/techshan](https://github.com/raushan2015/techshan)

### 📦 [TECHSHAN-IMS](https://ims.techshan.app) · inventory management software

A multi-tenant ERP and inventory system for retail and wholesale businesses: double-entry accounting, POS, warehouse management, manufacturing, HR/payroll and a customer-facing storefront, in the shop's own language and currency.

| | |
|---|---|
| **Clients** | Web dashboard, tenant storefronts, marketplace, Electron desktop that works offline and syncs, Expo mobile app |
| **Backend** | 189 controllers · 140 services · public API with 122 routes · 64 integration test suites |
| **Database** | 339 tables · 141 migrations · PostgreSQL row-level security for tenant isolation |
| **Stack** | TypeScript · Node.js · Express · Next.js · React · PostgreSQL · Redis · BullMQ · MinIO · Electron · Expo · Docker |

🔗 [ims.techshan.app](https://ims.techshan.app)

## Home lab

TECHSHAN-IMS runs in production on a home lab I built and look after by myself: Linux, Docker, an Nginx reverse proxy with SSL/TLS, Pi-hole for DNS, VPN for remote access, with automated backups and deployments.

```mermaid
flowchart LR
    U([Internet]) --> CF[Cloudflare DNS]
    CF --> R[Router<br/>Port-forward + Firewall]
    V([VPN client]) --> R
    R --> H[Linux host]
    H --> N[Nginx<br/>Reverse proxy + SSL]
    H --> PH[Pi-hole DNS]
    N --> APP[TECHSHAN · TECHSHAN-IMS · Plex]
    APP --> DB[(PostgreSQL · Redis · MinIO)]
```

When something breaks I don't guess. I check layer by layer (process → port → DNS → router → ISP), fix it, write down what happened, and automate the fix.

## Education and certifications

| | |
|---|---|
| **Global Information Career Academy** (Japan) | Information Systems · 2025 – 2027 |
| **Tokyo Management College, Global Study Center** (Japan) | Japanese language · 2023 – 2025 |
| **Reliance International Academy** (Nepal) | +2 (Higher Secondary) · 2016 – 2018 |
| **TOEIC 835** · **JLPT N3** | 2024 |

<p align="center">
  <a href="https://techshan.app"><img src="https://img.shields.io/badge/TECHSHAN-techshan.app-16a34a?style=flat-square&logo=linux&logoColor=white" alt="TECHSHAN" /></a>
  <a href="https://www.raushan7.com.np"><img src="https://img.shields.io/badge/Portfolio-raushan7.com.np-0ea5e9?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
  <a href="mailto:mail@raushan7.com.np"><img src="https://img.shields.io/badge/Email-mail%40raushan7.com.np-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://www.linkedin.com/in/raushan2015"><img src="https://img.shields.io/badge/LinkedIn-raushan2015-0A66C2?style=flat-square" alt="LinkedIn" /></a>
  <a href="https://instagram.com/raushan.2015"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="https://facebook.com/raushanchy7"><img src="https://img.shields.io/badge/Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white" alt="Facebook" /></a>
</p>
