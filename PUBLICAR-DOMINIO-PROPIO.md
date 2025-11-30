# 🌐 Cómo Publicar en Tu Dominio Propio

Ya tienes un dominio registrado. Esta guía te muestra cómo publicar tu sitio de Trading y Forex en ese dominio.

---

## 🎯 Opciones de Hosting

Tienes varias opciones, desde **gratis** hasta **pago** con más control:

| Opción | Costo | Dificultad | Recomendado Para |
|--------|-------|------------|------------------|
| **Netlify** | Gratis | ⭐ Fácil | Principiantes |
| **Vercel** | Gratis | ⭐ Fácil | Principiantes |
| **Cloudflare Pages** | Gratis | ⭐⭐ Media | Todos |
| **Hosting Compartido** | $3-10/mes | ⭐⭐ Media | Necesitas email |
| **VPS** | $5-20/mes | ⭐⭐⭐ Avanzada | Proyectos grandes |

---

## 🚀 MÉTODO 1: Netlify (Recomendado - GRATIS)

Netlify es perfecto para sitios estáticos. Ofrece hosting gratis, SSL, CDN global y deploy automático.

### **Paso 1: Crear Cuenta en Netlify**

1. Ve a [https://www.netlify.com](https://www.netlify.com)
2. Clic en **"Sign up"**
3. Regístrate con GitHub, GitLab, o email

### **Paso 2: Deploy Tu Sitio**

**Opción A: Drag & Drop (Más Fácil)**

1. En Netlify Dashboard, busca **"Sites"**
2. **Arrastra la carpeta** `trading-forex-blog/` completa a la zona que dice "Drag and drop your site folder here"
3. Espera 30 segundos
4. ✅ **¡Publicado!**

Tu sitio estará en: `https://nombre-aleatorio.netlify.app`

**Opción B: Conectar con GitHub (Mejor para actualizaciones)**

1. En Netlify, clic en **"New site from Git"**
2. Conecta con GitHub
3. Selecciona el repositorio `trading-forex-blog`
4. Configuración:
   - **Branch:** `main`
   - **Build command:** (dejar vacío)
   - **Publish directory:** `./`
5. Clic en **"Deploy site"**

✅ **Ventaja:** Cada vez que actualices GitHub, Netlify actualiza automáticamente.

### **Paso 3: Conectar Tu Dominio Propio**

1. En Netlify, ve a **Site settings → Domain management**
2. Clic en **"Add custom domain"**
3. Escribe tu dominio: `tradingdesdecero.com`
4. Netlify te dará instrucciones DNS

### **Paso 4: Configurar DNS**

En tu proveedor de dominio (GoDaddy, Namecheap, etc.):

**Si quieres usar `tradingdesdecero.com` (sin www):**
1. Crea registro **A** (apex):
   - **Host:** `@`
   - **Value:** `75.2.60.5`

**Si quieres usar `www.tradingdesdecero.com`:**
1. Crea registro **CNAME**:
   - **Host:** `www`
   - **Value:** `nombre-tu-sitio.netlify.app`

2. Redirección (opcional):
   - Redirige `tradingdesdecero.com` → `www.tradingdesdecero.com`

### **Paso 5: Activar SSL (HTTPS)**

1. En Netlify → Domain management
2. Scroll a **HTTPS**
3. Clic en **"Verify DNS configuration"**
4. Luego **"Provision certificate"**
5. Espera 1-5 minutos

✅ **¡Listo! Tu sitio está en:** `https://tradingdesdecero.com`

---

## ⚡ MÉTODO 2: Cloudflare Pages (GRATIS + CDN)

Cloudflare Pages es similar a Netlify pero con el poder del CDN de Cloudflare.

### **Paso 1: Crear Cuenta**

1. Ve a [https://pages.cloudflare.com](https://pages.cloudflare.com)
2. Regístrate gratis

### **Paso 2: Crear Proyecto**

1. Clic en **"Create a project"**
2. Conecta con GitHub
3. Selecciona `trading-forex-blog`
4. Configuración:
   - **Production branch:** `main`
   - **Build command:** (vacío)
   - **Build output directory:** `/`
5. **"Save and Deploy"**

### **Paso 3: Dominio Personalizado**

1. En Pages, ve a **Custom domains**
2. Clic **"Set up a custom domain"**
3. Escribe `tradingdesdecero.com`
4. Cloudflare configura DNS automáticamente (si tu dominio está en Cloudflare)

**Si tu dominio NO está en Cloudflare:**

1. Cambia los nameservers de tu dominio a Cloudflare
2. Cloudflare te dará 2 nameservers (ej: `eva.ns.cloudflare.com`)
3. En tu registrador de dominio, cambia DNS a esos nameservers

---

## 💻 MÉTODO 3: Hosting Compartido (cPanel)

Si ya tienes hosting compartido (Hostinger, Bluehost, SiteGround, etc.) con cPanel:

### **Paso 1: Acceder a cPanel**

1. Inicia sesión en tu hosting
2. Abre **cPanel**

### **Paso 2: Subir Archivos**

**Opción A: File Manager**

1. En cPanel, abre **File Manager**
2. Navega a `public_html/` (o `www/`)
3. **Elimina** archivos por defecto (index.html, etc.)
4. Clic en **"Upload"**
5. Sube TODOS los archivos de `trading-forex-blog/`:
   - `index.html`
   - Carpeta `css/`
   - Carpeta `articulos/`
   - `README.md`

**Opción B: FTP (FileZilla)**

1. Descarga [FileZilla](https://filezilla-project.org/)
2. Conéctate con credenciales FTP:
   - **Host:** ftp.tudominio.com
   - **Usuario:** tu usuario FTP
   - **Contraseña:** tu contraseña FTP
   - **Puerto:** 21
3. En **Remote site**, navega a `/public_html/`
4. En **Local site**, selecciona `trading-forex-blog/`
5. Arrastra todos los archivos de local a remote

### **Paso 3: SSL (HTTPS)**

1. En cPanel, busca **SSL/TLS Status**
2. Selecciona tu dominio
3. Clic en **"Run AutoSSL"**
4. Espera 5 minutos

### **Paso 4: Forzar HTTPS (Opcional)**

Crea/edita `.htaccess` en `public_html/`:

```apache
# Forzar HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Forzar www (opcional)
RewriteCond %{HTTP_HOST} !^www\.
RewriteRule ^(.*)$ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

✅ **Tu sitio está en:** `https://tudominio.com`

---

## 🔧 MÉTODO 4: VPS (Avanzado - Mejor Performance)

Si esperas mucho tráfico (100k+ visitas/mes) o quieres control total.

### **Proveedores Recomendados:**

- **DigitalOcean:** $6/mes (Droplet básico)
- **Vultr:** $5/mes
- **Linode:** $5/mes
- **Hetzner:** €4.5/mes (muy barato)

### **Configuración Básica (Ubuntu + Nginx)**

```bash
# 1. Conectar por SSH
ssh root@tu-ip-del-vps

# 2. Actualizar sistema
apt update && apt upgrade -y

# 3. Instalar Nginx
apt install nginx -y

# 4. Instalar Certbot (SSL)
apt install certbot python3-certbot-nginx -y

# 5. Crear carpeta del sitio
mkdir -p /var/www/tradingdesdecero.com/html

# 6. Subir archivos (vía FTP/SFTP o Git)
# Sube todos tus archivos a /var/www/tradingdesdecero.com/html/

# 7. Configurar Nginx
nano /etc/nginx/sites-available/tradingdesdecero.com
```

**Contenido del archivo:**

```nginx
server {
    listen 80;
    server_name tradingdesdecero.com www.tradingdesdecero.com;
    root /var/www/tradingdesdecero.com/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Caché para archivos estáticos
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

```bash
# 8. Activar sitio
ln -s /etc/nginx/sites-available/tradingdesdecero.com /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

# 9. Obtener SSL gratis
certbot --nginx -d tradingdesdecero.com -d www.tradingdesdecero.com

# 10. Configurar DNS
# En tu registrador de dominio:
# A record: @ → tu-ip-del-vps
# A record: www → tu-ip-del-vps
```

✅ **Sitio en:** `https://tradingdesdecero.com`

---

## 📊 Comparación de Opciones

| Característica | Netlify | Cloudflare Pages | Hosting cPanel | VPS |
|----------------|---------|------------------|----------------|-----|
| **Costo** | Gratis | Gratis | $3-10/mes | $5-20/mes |
| **SSL** | ✅ Gratis | ✅ Gratis | ✅ Gratis | ✅ Gratis (Certbot) |
| **CDN** | ✅ Incluido | ✅ Incluido | ❌ Depende | ❌ Manual |
| **Deploy automático** | ✅ Sí | ✅ Sí | ❌ No | ❌ No |
| **Email** | ❌ No | ❌ No | ✅ Sí | ✅ Sí (manual) |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dificultad** | ⭐ Fácil | ⭐ Fácil | ⭐⭐ Media | ⭐⭐⭐⭐ Difícil |

---

## 🎯 Mi Recomendación

### **Para Empezar (0-10k visitas/mes):**
👉 **Netlify** - Gratis, fácil, rápido

### **Para Crecer (10k-100k visitas/mes):**
👉 **Cloudflare Pages** - CDN global, gratis, excelente performance

### **Si necesitas email:**
👉 **Hosting cPanel** (Hostinger, SiteGround)

### **Para escalar (100k+ visitas/mes):**
👉 **VPS** (DigitalOcean, Vultr)

---

## ⚙️ Configuraciones Posteriores

### **1. Optimizar Velocidad**

**Comprimir imágenes:**
- Usa [TinyPNG](https://tinypng.com/)
- Guarda en `/images/` con nombres descriptivos

**Minificar CSS:**
```bash
# Si quieres minificar (opcional)
# Usa: https://cssminifier.com/
# Pega tu CSS, copia el minificado, crea style.min.css
```

### **2. Google Search Console**

1. Ve a [Google Search Console](https://search.google.com/search-console)
2. Añade tu propiedad: `https://tudominio.com`
3. Verifica propiedad (método HTML tag o DNS)
4. Envía sitemap: `https://tudominio.com/sitemap.xml`

### **3. Google Analytics**

1. Crea cuenta en [Google Analytics](https://analytics.google.com/)
2. Obtén código de tracking
3. Añade antes de `</head>` en todos tus HTML

### **4. AdSense**

1. Aplica a [Google AdSense](https://www.google.com/adsense)
2. Espera aprobación (1-2 semanas)
3. Reemplaza placeholders con códigos reales
4. Sube archivos actualizados

---

## 🐛 Solución de Problemas

### "Dominio no resuelve"

**Solución:**
- Espera 24-48 horas (propagación DNS)
- Verifica DNS con [DNS Checker](https://dnschecker.org/)
- Confirma que records A/CNAME estén correctos

### "CSS no carga"

**Solución:**
- Verifica rutas relativas en HTML
- Asegúrate que archivos `.css` se subieron
- Revisa permisos (644 para archivos, 755 para carpetas)

### "Sitio carga pero sin estilos"

**Solución:**
- Abre consola del navegador (F12)
- Revisa errores de red (Network tab)
- Verifica que `css/style.css` exista en el servidor

---

## ✅ Checklist Final

Antes de lanzar:

- [ ] Dominio apunta correctamente (DNS configurado)
- [ ] SSL activo (https://)
- [ ] Todos los archivos subidos
- [ ] CSS/JS cargan correctamente
- [ ] Navegación funciona
- [ ] Artículos abren
- [ ] Responsive en móvil
- [ ] Google Analytics instalado
- [ ] Google Search Console configurado
- [ ] Velocidad de carga < 3 segundos

---

## 📈 Próximos Pasos

1. ✅ **Publica tu sitio**
2. ✅ **Crea más contenido** (objetivo: 50-100 artículos)
3. ✅ **SEO on-page** (meta tags, keywords)
4. ✅ **Promoción** (redes sociales, foros)
5. ✅ **AdSense** (aplica cuando tengas 30+ artículos)
6. ✅ **Monitorea** (Analytics, Search Console)

---

**¡Tu sitio de Trading y Forex está listo para generar ingresos!** 🚀

---

*Última actualización: Enero 2025*
