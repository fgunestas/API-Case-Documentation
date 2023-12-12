# Stable Diffusion API Documentation

Verilen bilgiler doğrultusunda afiş hazırlayan API servisi.

## API Kullanımı

API'yi kullanmak için aşağıdaki endpoint'leri kullanabilirsiniz.

### Endpoint: `/api/AdGenerator`

**HTTP Metodu:** POST

**Açıklama:** İki PNG dosyası ve üç metin parametresi alır, işlemleri gerçekleştirir ve bir PNG dosyası olarak yanıt verir.

### Parametreler:

- `Image_`: Oluşturulacak yeni görseli ilgilendiren PNG dosyası (binary)
- `Logo`: En üstte yer alacak ürün/müşteri PNG logosu. (binary)
- `Prompt`: Üretilecek yeni görselin tanımlama metni. (string)
- `Renk1`: Üretilecek yeni görselde bulunacak rengin Hex kodu (string)
- `Renk2`: Afişin altında bulunacak buton ve metnin rengi. (string)
- `Punchline`: Afişin altında bulunacak metin. (string)
- `Button`: Afişin altında bulunan butonun metni (string)

### Örnek Kullanım:

```bash
curl -X POST -H "Content-Type: multipart/form-data" 
-F "Image_=@C:\Users\shu\Downloads\Untitled.png;type=image/png" 
-F "Logo=@C:\Users\shu\Desktop\Coca-Cola_logo.svg.png;type=image/png" 
-F "Prompt=a cup of coffee" -F "Renk1=#81d8d0" -F "Renk2=#81d8d0" 
-F "Punchline=Lorem ipsum dolor sit amet, consectetur adipiscing elit." 
-F "Button=Click Me" 
http://95.70.170.173:32703/api/Ad_Generator 
--output output_image.png
```
### Örnek Yanıt:

Bir PNG dosyası olarak yanıt verir. Yanıt, işlemler sonucunda oluşturulan resmi içerir.

### Notlar:
*Image_* ve *Logo* parametreleri, file olarak gönderilmelidir.
Parametreler JSON formatında değil, form verisi olarak gönderilmelidir.
Yanıt olarak alınan PNG dosyası, isteğe bağlı olarak kaydedilebilir.
