# Generated by Django 2.2.11 on 2020-04-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200424_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程信息表', 'verbose_name_plural': '课程信息表'},
        ),
        migrations.AlterModelOptions(
            name='coursearrangement',
            options={'verbose_name': '课程安排表', 'verbose_name_plural': '课程安排表'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': '消息表', 'verbose_name_plural': '消息表'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '公告表', 'verbose_name_plural': '公告表'},
        ),
        migrations.AlterModelOptions(
            name='schoolterm',
            options={'verbose_name': '学期表', 'verbose_name_plural': '学期表'},
        ),
        migrations.AlterModelOptions(
            name='selectcourse',
            options={'verbose_name': '选课表', 'verbose_name_plural': '选课表'},
        ),
        migrations.AlterModelOptions(
            name='selectlist',
            options={'verbose_name': '选课清单表', 'verbose_name_plural': '选课清单表'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生信息表', 'verbose_name_plural': '学生信息表'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教师信息表', 'verbose_name_plural': '教师信息表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户登录表', 'verbose_name_plural': '用户登录表'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='student_graduate_school',
            new_name='teacher_graduate_school',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_college',
            field=models.CharField(choices=[('1', '信息科学与技术学院'), ('2', '材料科学与工程学院'), ('3', '机电工程学院'), ('4', '化学工程学院'), ('5', '经济管理学院'), ('6', '化学学院'), ('7', '数理学院'), ('8', '文法学院'), ('9', '生命科学与技术学院'), ('10', '继续教育学院'), ('11', '马克思主义学院'), ('12', '国际教育学院'), ('13', '侯德榜工程师学院'), ('14', '巴黎居里工程师学院')], default='信息科学与技术', max_length=20, verbose_name='开课学院'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='课程名'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='消息号'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发送日期'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='通知号'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发送日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_age',
            field=models.PositiveSmallIntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birthday',
            field=models.DateField(verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_college',
            field=models.CharField(choices=[('1', '信息科学与技术学院'), ('2', '材料科学与工程学院'), ('3', '机电工程学院'), ('4', '化学工程学院'), ('5', '经济管理学院'), ('6', '化学学院'), ('7', '数理学院'), ('8', '文法学院'), ('9', '生命科学与技术学院'), ('10', '继续教育学院'), ('11', '马克思主义学院'), ('12', '国际教育学院'), ('13', '侯德榜工程师学院'), ('14', '巴黎居里工程师学院')], default='信息科学与技术学院', max_length=20, verbose_name='学院'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_come_year',
            field=models.DateField(verbose_name='入学日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_foreign_language',
            field=models.CharField(choices=[('1', '英语'), ('2', '法语'), ('3', '日语'), ('4', '俄语')], default='英语', max_length=20, verbose_name='外语'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_nation',
            field=models.CharField(choices=[('1', '汉族'), ('2', '满族'), ('3', '回族'), ('4', '藏族'), ('5', '维吾尔族'), ('6', '苗族'), ('7', '彝族'), ('8', '壮族'), ('9', '布依族'), ('10', '侗族'), ('11', '瑶族'), ('12', '白族'), ('14', '土家族'), ('15', '哈尼族'), ('16', '哈萨克族'), ('17', '傣族'), ('18', '傈僳族'), ('19', '佤族'), ('20', '畲族'), ('21', '高山族'), ('22', '拉祜族'), ('23', '水族'), ('24', '东乡族'), ('25', '纳西族'), ('26', '景颇族'), ('27', '柯尔克孜族'), ('28', '土族'), ('29', '达斡尔族'), ('30', '仫佬族'), ('31', '羌族'), ('32', '布朗族'), ('33', '撒拉族'), ('34', '毛南族'), ('35', '仡佬族'), ('36', '锡伯族'), ('37', '阿昌族'), ('38', '普米族'), ('39', '朝鲜族'), ('40', '塔吉克族'), ('41', '怒族'), ('42', '乌孜别克族'), ('43', '俄罗斯族'), ('44', '鄂温克族'), ('45', '德昂族'), ('46', '保安族'), ('47', '裕固族'), ('48', '京族'), ('49', '塔塔尔族'), ('50', '独龙族'), ('51', '鄂伦春族'), ('52', '赫哲族'), ('53', '门巴族'), ('54', '珞巴族'), ('55', '基诺族'), ('56', '黎族')], default='汉族', max_length=20, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_political_status',
            field=models.CharField(choices=[('1', '中共党员'), ('2', '共青团员'), ('3', '群众')], default='群众', max_length=20, verbose_name='政治面貌'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_status',
            field=models.CharField(choices=[('1', '在读'), ('2', '毕业')], default='在读', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_academic_title',
            field=models.CharField(choices=[('1', '助教'), ('2', '讲师'), ('3', '副教授'), ('4', '教授')], default='教授', max_length=20, verbose_name='职称'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_age',
            field=models.PositiveSmallIntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_degree',
            field=models.CharField(choices=[('1', '学士'), ('2', '硕士'), ('3', '博士')], default='学士', max_length=20, verbose_name='学位'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_nation',
            field=models.CharField(choices=[('1', '汉族'), ('2', '满族'), ('3', '回族'), ('4', '藏族'), ('5', '维吾尔族'), ('6', '苗族'), ('7', '彝族'), ('8', '壮族'), ('9', '布依族'), ('10', '侗族'), ('11', '瑶族'), ('12', '白族'), ('14', '土家族'), ('15', '哈尼族'), ('16', '哈萨克族'), ('17', '傣族'), ('18', '傈僳族'), ('19', '佤族'), ('20', '畲族'), ('21', '高山族'), ('22', '拉祜族'), ('23', '水族'), ('24', '东乡族'), ('25', '纳西族'), ('26', '景颇族'), ('27', '柯尔克孜族'), ('28', '土族'), ('29', '达斡尔族'), ('30', '仫佬族'), ('31', '羌族'), ('32', '布朗族'), ('33', '撒拉族'), ('34', '毛南族'), ('35', '仡佬族'), ('36', '锡伯族'), ('37', '阿昌族'), ('38', '普米族'), ('39', '朝鲜族'), ('40', '塔吉克族'), ('41', '怒族'), ('42', '乌孜别克族'), ('43', '俄罗斯族'), ('44', '鄂温克族'), ('45', '德昂族'), ('46', '保安族'), ('47', '裕固族'), ('48', '京族'), ('49', '塔塔尔族'), ('50', '独龙族'), ('51', '鄂伦春族'), ('52', '赫哲族'), ('53', '门巴族'), ('54', '珞巴族'), ('55', '基诺族'), ('56', '黎族')], default='汉族', max_length=20, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_political_status',
            field=models.CharField(choices=[('1', '中共党员'), ('2', '共青团员'), ('3', '群众')], default='群众', max_length=20, verbose_name='政治面貌'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.SlugField(verbose_name='密码'),
        ),
    ]