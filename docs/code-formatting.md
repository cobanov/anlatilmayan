# Code Formatting

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|black| C[Hmm...];
  C --> D[isort];
  D --> B;
  B ---->|No| E[Yay!];
```

Python programlama dili belki de diğer dillerden farklı kılan önemli bir nokta, yazılan çok daha okunaklı olmasıdır. Yani, kodu okuması kolay bir biçimde yazmak her zaman daha ***pythonic*** bir yaklaşımdır. Fakat kod yazarken bu ince ayrıntılara her seferinde dikkat etmek biraz uğraştırıcı ve sıkıcı olabilir. Bu yüzden bazı araçlar kullanarak kod biçimlendirme işini otomatikleştiririz.

## black

**Black**, temelde bir kod formatlayıcıdır. Temel görevi, birden fazla geliştricisi bulunan bir projede kodun sanki tek bir kişi tarafından yazılmış gibi görünmesini sağlamaktır.Python kodları için resmi stil kılavuzu olan `PEP 8`'e sıkı sıkıya bağlıdır.

Genellikle yazılımcılar `vscode` veya benzer bir editör kullanırken dosyalarını her kaydettiklerinde otomatik olarak çalışaca şekilde ayarlar veya `sürekli entegrasyon (CI)` pipeline'ının bir parçası olarak kullanılır. Bu konuda `pre-commit-hook` kısmında bahsedeceğim.

### Kurulum (black)

Kurulum için `pip` veya `conda` kullanabiliriz:

```bash
pip install black

# for conda
conda install black
```

### Kullanım (black)

Aşağıdaki gibi bir kod bloğuna sahip olduğumuzu düşünelim. Bu birçok açıdan hatalı bir örnek, fakat çoğu zaman yazılımcıların alışkanlıkları farklı olabiliyor.

```py title="unformatted.py"
# Code source: https://towardsdatascience.com/treat-yourself-using-the-black-library-when-writing-python-code-7626b6099247
# file: code-example/formatted.py

def my_function(a=1,b=2,c=3,d=4):
    my_list = [a, 
               b, 
               c, 
               d]
    return sum(my_list)
if True: print(my_function())
```

Bunu standartlaştırmak için yapabileceğimiz en basit şey iste black kullanmak.

```shell
$ black code-example/formatted.py
# reformatted code-example/formatted.py

# All done! ✨ 🍰 ✨
# 1 file reformatted.
```

Son durumda kodumuz bu şekilde gözükecek.

```py title="formatted.py"
# file: code-example/formatted.py

def my_function(a=1, b=2, c=3, d=4):
    my_list = [a, b, c, d]
    return sum(my_list)


if True:
    print(my_function())
```

## isort

**isort,** Python importlarini alfabetik olarak sıralayan ve bunları bölümlere ve türe göre ayıran bir yardımcı kütüphanedir. Importlarin proje veya dosya boyunca temiz ve tutarlı bir şekilde yönetilmesini sağlar.

### Kurulum (isort)

Kurulum için `pip` veya `conda` kullanabiliriz:

```bash
pip install isort

# for conda
conda install isort
```

### Kullanım (isort)

Python dosyasında karışık ve düzensiz importlar içeren bir örnek.

```py title="unsorted.py"
from my_module import function_three
import os
from another_module import function_one, function_two
import sys
from third_module import (function_four,
                          function_five, function_six)
```

Aynı dosya `isort` kullanılarak yeniden düzenlendiğinde, içe aktarmalar **alfabetik sıraya göre** ve **uygun gruplara ayrılmış** olarak düzenlenir.

```py title="sorted.py"
import os
import sys

from another_module import function_one, function_two
from my_module import function_three
from third_module import function_four, function_five, function_six
```

Her iki araç da, kod formatlamayı otomatikleştirerek ve standartlaştırarak kod tabanlarını daha temiz, daha bakılabilir ve daha okunabilir hale getirdikleri için Python topluluğunda yaygın olarak benimsenmiştir. Bir projede farklı kod formatlama yönlerini ele almak için birlikte kullanılabilirler: Genel kod yapısı için Black ve içe aktarma ifadeleri için isort.

## Pre-commit hook

Ayrıca, düzgün biçimlendirilmemiş kodları yakalamak için `pre-commit-hook` kullanabiliriz ve kod biçimlendiricilerini çalıştırarak, herhangi bir biçimlendirme yapılması gerekiyorsa tamamını otomatikleştirebiliriz. Bu, yanlış biçimlendirilmiş kodu asla `commit` etmememizi sağlar.

`pre-commit-hook` konusuna başka bir derste değineceğim, ancak bu konuda nasıl kurulum yapılacağına dair diğer kaynakları araştırabilirsiniz.

## Further Reading & Sources

- <https://towardsdatascience.com/treat-yourself-using-the-black-library-when-writing-python-code-7626b6099247>
