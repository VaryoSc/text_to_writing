
# Make plausible handwriting texts, Now with Arabic support!

I am mearly making this file because the other available counterparts of it are no longer supported and because thi is tthe only one with typer cli and can handle both latin and arabic at the same time(altough it can be better)
It can be run using either typer cli and paramaters give by it or you could edit the texttowriting.py file for a more customized experience.
You need to add the fonts file for both latin and arabic texts to the projects base folder and set them at the respective files.

# متن های تاپیتو شبیه دست نویس بگیر، با پشتیبانی از زبون فارسی!!!

یک فایل پایتون ساده که متنی که بهش میدی رو تو فرمت ی عکس با همون متنا روش رو بهت میده
برای استفاده فونتای خودتو بزار کنار فایل برنامه و برنامه رو از طریق کنسول بالا بیار یا اگه خواصتی
میتونی فایل 
texttowriting.py
رو خودت ادیت و ران کنی
پیشنهاد من فونت دست نویسه
https://www.fontyab.com/1878/dastnevis.html
## Typer CLI API Reference

#### Get Parameter Info

```cli
   python3 typetotext.py -help
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `help` | `string` | **Required** |

#### Get image file

```cli
   python3 typetotext.py
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `string` |  The text you wanna write |
| `arabicfont`      | `string` |  The font name for arabic texts example: danstevis.otf |
| `englishfont`      | `string` | The font name for latin texts example: danstevis.ttf |
| `positionx`      | `string` |  The starting points width |
| `positiony`      | `string` |  The starting points hight |
| `arabic-align`      | `string` |  The alignment for arabic text  |
| `english-align `      | `string` |  The alignment for latin text |
| `fill`      | `string` |  Write the color you want typer hasn't added tuple support |



## Deployment

It needs python version 3.11 or higher

```bash
$ pip install Pillow
$ python3 texttowriting.py
```
The following are only needed for typer cli interactions

```bash
$ pip install typer
$ python3 typetotext.py
```
