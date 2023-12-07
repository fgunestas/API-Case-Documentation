# Stable Diffusion API Documentation

Verilen bilgiler doğrultusunda afiş hazırlayan API servisi.

## API Kullanımı

API'yi kullanmak için aşağıdaki endpoint'leri kullanabilirsiniz.

### Endpoint: `/api/process_images`

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
curl -X POST -F "Image_=@image1.png" -F "Logo=@image2.png" -F "Prompt=a cup of coffee" -F "Renk1=#FFFFFF" -F "Renk2=#FFFFFF" -F "Punchline=Lorem ipsum dolor sit amet." -F "Button=Click me" http://localhost:5000/api/process_images
```
### Örnek Yanıt:

Bir PNG dosyası olarak yanıt verir. Yanıt, işlemler sonucunda oluşturulan resmi içerir.

### Notlar:
*Image_* ve *Logo* parametreleri, binary olarak gönderilmelidir.
Parametreler JSON formatında değil, form verisi olarak gönderilmelidir.
Yanıt olarak alınan PNG dosyası, isteğe bağlı olarak kaydedilebilir veya başka bir işleme tabi tutulabilir.
