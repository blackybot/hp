import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import MagicManager


client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print(client.user.id)
    print("시작")
    game = discord.Game("/도움말")

    await client.change_presence(status=discord.Status.online, activity=game)   

    MagicManager.init()
    MagicManager.ChangeSetting(1,1,30,20,30)
    MagicManager.RegistMagic("윙가르디움레비오우사",10,1,5)
    MagicManager.RegistMagic("루모스",20,2,10)
    MagicManager.RegistMagic("녹스", 20, 2, 10)
    MagicManager.RegistMagic("루모스 맥시마",30,3,15)
    MagicManager.RegistMagic("루모스 솔렘",40,4,20)
    MagicManager.RegistMagic("스투페파이",80,20,30)
    MagicManager.RegistMagic("레네르바테",80,20,30)
    MagicManager.RegistMagic("붐바르다",140,30,100)
    MagicManager.RegistMagic("레파로", 1, 5, 1)
    MagicManager.RegistMagic("리덕토", 30, 9, 15)
    MagicManager.RegistMagic("레벨업용", 1, 1, 10000000000)
    MagicManager.RegistMagic("잉고르지오", 35, 6, 15)
    MagicManager.RegistMagic("리듀시오", 35, 7, 15)
    MagicManager.RegistMagic("라카르눔 인플라모레", 60, 10, 20)
    MagicManager.RegistMagic("인센디오", 30, 8, 10)
    MagicManager.RegistMagic("모스모드레", 1000, 1000, -100000)
    MagicManager.RegistMagic("페트리피쿠스 토탈루스", 30, 15, 20)
    MagicManager.RegistMagic("마법추가", 0, 0, 0)
    MagicManager.RegistMagic("서버", 0, 0, 0)
    MagicManager.RegistMagic("프로테고", 50, 25, 0)

    


'''
@client.event
async def on_message(message):
    await client.process_commands(message)
'''



@client.event
async def on_message(message):
    ErrorMessage = ["마나가 부족합니다\n마나회복후 다시 시도해주세요", "레벨이 부족합니다\n레벨을 올린 후 시도해주세요"]
    LevelUpMessage = "님이 레벨업 하셨습니다"
    if message.content.startswith("/루모스"):
        r = MagicManager.UseMagic(message.author.id,"루모스")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("느린섬광탄.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/루 맥시마"):
        r = MagicManager.UseMagic(message.author.id,"루모스 맥시마")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("섬광탄.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/루 솔렘"):
        r = MagicManager.UseMagic(message.author.id,"루모스 솔렘")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("섬광.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/윙가르디움레비오우사"):
        r = MagicManager.UseMagic(message.author.id,"윙가르디움레비오우사")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(둥실둥실)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/레네르바테'):
        r = MagicManager.UseMagic(message.author.id,"레네르바테")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member(int(message.content[9:27]))
            role = discord.utils.get(message.guild.roles, name="기절")
            await author.remove_roles(role)
            await message.channel.send("<@" + str(author.id) + ">가 깨어났다.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/스투페파이'):
        r = MagicManager.UseMagic(message.author.id,"스투페파이")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            if MagicManager.GetImformation(message.content[9:27], "D1") == 0:
                author = message.guild.get_member(int(message.content[9:27]))
                role = discord.utils.get(message.guild.roles, name="기절")
                await author.add_roles(role)
                await message.channel.send("<@" + str(author.id) + ">가 기절했다.")
            else:
                MagicManager.ChangeImformation(message.content[9:27], "D1", 0)
                await message.channel.send("<@" + str(message.content[9:27]) + ">가 방어했다.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/프로테고'):
        r = MagicManager.UseMagic(message.author.id,"프로테고")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member(int(message.content[8:26]))
            MagicManager.ChangeImformation(message.content[8:26], "D1", 1)
            role = discord.utils.get(message.guild.roles, name="보호막")
            await message.channel.send("<@" + str(author.id) + ">에게 보호막이 생성되었다 \n (보호막은 1회용이며 자신을 겨냥한 모든 주문으로부터 보호됩니다.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/붐바르다'):
        r = MagicManager.UseMagic(message.author.id,"붐바르다")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            text = message.content.split(" ")
            await message.channel.purge(limit=int(text[1]))
            await message.channel.send(text[1] + "개의 메세지를 파괴했습니다.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/레파로"):
        r = MagicManager.UseMagic(message.author.id,"레파로")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("('어떤 것'이 붙었다.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/리덕토"):
        r = MagicManager.UseMagic(message.author.id,"리덕토")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.delete()
            await message.channel.send("(메세지 1개가 파괴되었습니다.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/레벨업"):
        r = MagicManager.UseMagic(message.author.id,"레벨업용")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(븪)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/잉고르지오"):
        r = MagicManager.UseMagic(message.author.id,"잉고르지오")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("('어떤 것'이 커졌다.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/리듀시오"):
        r = MagicManager.UseMagic(message.author.id,"리듀시오")
        if r == -10:
            print("함수 이름 오류")
        if r== -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("('어떤 것'이 작아졌다.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/라카르눔 인플라모레"):
        r = MagicManager.UseMagic(message.author.id, "라카르눔 인플라모레")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("라카르눔 인플라모레.jpg"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/인센디오"):
        r = MagicManager.UseMagic(message.author.id, "인센디오")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("인센디오.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/테스트"):
        r = MagicManager.UseMagic(message.author.id, "테스트")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(븪)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/모스모드레"):
        r = MagicManager.UseMagic(message.author.id, "모스모드레")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("모스모드레.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/마법추가"):
        r = MagicManager.UseMagic(message.author.id, "마법추가")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("https://forms.gle/2k6FYZtuWpuZ12BQ9")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/서버"):
        r = MagicManager.UseMagic(message.author.id, "서버")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("https://discord.gg/jF6s47J")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/페트리피쿠스 토탈루스'):
        r = MagicManager.UseMagic(message.author.id, "페트리피쿠스 토탈루스")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member(int(message.content[15:33]))
            role = discord.utils.get(message.guild.roles, name="동작그만")
            await author.add_roles(role)
            await message.channel.send("<@" + str(author.id) + ">가 석화되었다.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/위키"):
        r = MagicManager.UseMagic(message.author.id, "서버")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("https://namu.wiki/w/%ED%95%B4%EB%A6%AC%ED%8F%AC%ED%84%B0%20%EB%B4%87")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)

    if message.content.startswith('/정보'):
        embed = discord.Embed(title=message.guild.get_member(int(message.author.id)).name+"님의 정보", description="정보", color=800080)
        embed.add_field(name="레벨", value=str(MagicManager.GetImformation(message.author.id,"L")), inline=False)
        embed.add_field(name="현재 마나", value=str(MagicManager.GetImformation(message.author.id,"M")), inline=False)
        embed.add_field(name="최대 마나", value=str(MagicManager.GetImformation(message.author.id,"MM")), inline=False)
        embed.add_field(name="경험치", value=str(MagicManager.GetImformation(message.author.id,"PE"))+"/"+str(MagicManager.GetImformation(message.author.id,"NE")), inline=False)
        embed.add_field(name="total 경험치", value=str(MagicManager.GetImformation(message.author.id,"TE")), inline=False)
        embed.add_field(name="방어막 개수", value=str(MagicManager.GetImformation(message.author.id, "D1")), inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/도움말"):
        embed = discord.Embed(title="도움말", description="해리포터 봇 도움말입니다", color=800080)
        embed.add_field(name="어떤 주문이 있는지 알고 싶을 땐?", value="/주문 도움말", inline=False)
        embed.add_field(name="어떤 명령어가 있는지 알고 싶을 땐?", value="/명령어 도움말", inline=False)
        embed.add_field(name="만약 서버의 관리자라면?", value="/관리자 도움말", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/주문 도움말"):
        embed = discord.Embed(title="주문 도움말", description="사용가능 주문 목록입니다.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="1레벨 사용가능 주문", value="/윙가르디움 레비오우사", inline=False)
        embed.add_field(name="2레벨 사용가능 주문", value="/루모스", inline=False)
        embed.add_field(name="3레벨 사용가능 주문", value="/루 맥시마", inline=False)
        embed.add_field(name="4레벨 사용가능 주문", value="/루 솔렘", inline=False)
        embed.add_field(name="5레벨 사용가능 주문", value="/레파로", inline=False)
        embed.add_field(name="6레벨 사용가능 주문", value="/잉고르지오", inline=False)
        embed.add_field(name="7레벨 사용가능 주문", value="/리듀시오", inline=False)
        embed.add_field(name="8레벨 사용가능 주문", value="/인센디오", inline=False)
        embed.add_field(name="9레벨 사용가능 주문", value="/리덕토", inline=False)
        embed.add_field(name="10레벨 사용가능 주문", value="/라카르눔 인플라모레", inline=False)
        embed.add_field(name="15레벨 사용가능 주문", value="/페트리피쿠스 토탈루스", inline=False)
        embed.add_field(name="20레벨 사용가능 주문", value="/스투페파이 , /레네르바테", inline=False)
        embed.add_field(name="25레벨 사용가능 주문", value="/프로테고", inline=False)
        embed.add_field(name="30레벨 사용가능 주문", value="/붐바르다", inline=False)
        embed.add_field(name="주문 추가 방법", value="/마법추가", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/명령어 도움말"):
        embed = discord.Embed(title="명령어 도움말", description="사용가능 명령어 목록입니다.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="사용자 정보 확인", value="/정보", inline=False)
        embed.add_field(name="마나 정보 확인", value="/마나", inline=False)
        embed.add_field(name="업데이트 확인 `beta`", value="/업데이트", inline=False)
        embed.add_field(name="공식 디스코드 서버", value="/서버", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/관리자 도움말"):
        embed = discord.Embed(title="관리자 도움말", description="초기 세팅 방법입니다.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="봇 역할 세팅", value="관리자 권한을 봇에게 주셔야합니다.", inline=False)
        embed.add_field(name="기절 역할 세팅", value="봇의 하위 역할로 기절 역할을 만들어주시고 메세지 쓰기 및 보기를 해제해주세요.", inline=False)
        embed.add_field(name="동작그만 역할 세팅", value="봇의 하위 역할로 동작그만 역할을 만들어주시고 메세지 쓰기를 해제해주세요.", inline=False)
        embed.add_field(name="위의 두 역할 세팅", value="모든 역할은 봇의 하위 역할로 지정해야 하며 이름이 정확해야 합니다.", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/업데이트"):
        embed = discord.Embed(title="해리포터 봇 업데이트", description="~~자세한 업데이트 내용은 나무위키 참조~~", color=800080)
        embed.add_field(name="`현재 버전`", value="`beta 1.0v`", inline=False)
        embed.add_field(name="~~beta 이전 업데이트~~", value="추후 공개", inline=False)
        embed.add_field(name="해리포터 봇 beta버전 공개", value="beta 1.0v", inline=False)
        embed.add_field(name="Magicmanager 0.4v 업데이트", value="beta 1.0v", inline=False)
        embed.add_field(name="Magicmanager 0.4.1v 업데이트", value="beta 1.0v", inline=False)
        embed.add_field(name="beta 1.1v 업데이트 시작", value="beta 1.1 prerelease", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/마나"):
        embed = discord.Embed(title=message.guild.get_member(int(message.author.id)).name + "님의 마나", description="마나", color=800080)
        embed.add_field(name="현재 마나", value=str(MagicManager.GetImformation(message.author.id, "M")), inline=False)
        embed.add_field(name="최대 마나", value=str(MagicManager.GetImformation(message.author.id, "MM")), inline=False)
        await message.channel.send(embed=embed)



client.run("NzAxOTQ2MDg1MDUyMTIxMTg5.XrSwgg.DERWepL_r6USOSLr1TZIKffDOjQ")

