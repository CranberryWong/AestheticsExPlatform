#!/usr/bin/env python3
# -*- coding: utf-8 -*-

WebpageList = [
#'999*ted.com',
    '0*theboneandjointcenter.com',
    '1*theborneopost.com',
    '2*two-n.com',
    '3*swellnet.com',
    '4*klex.ru',    
    '5*disney.co.jp',
    '6*wikipedia.org',
    '7*news.yahoo.co.jp',
    '8*huxiu.com',
    '9*chi2019.acm.org',    
    '10*cheshi.com',
    '11*humblebundle.com',
    '12*theatlantic.com',
    '13*cvpr2018.thecvf.com',   
    '14*microsoft.com',
    '15*opera.com',
    '16*labinthewild.org',
    '17*macg.co',    
    '18*richyli.com',
    '19*pxtoem.com', 
    '20*dna.fr',    
    '21*javadrive.jp',
    '22*jcr.incites.thomsonreuters.com',
    '23*infoq.com',    
    '24*jiqimao.tv',
    '25*clamav.net',
    '26*bootcdn.cn',
    '27*runoob.com',
    '28*tensorfly.cn',
    '29*journaldugeek.com', 
    '30*matetranslate.com',
    '31*kameisyouten.ocnk.net',
    '32*gingerweb.jp',
    '33*cp.pocky.jp',
    '34*aladdin-aic.com',
    '35*trafst.jp',
    '36*cps.com.cn',
    '37*techplay.jp',    
    '38*kokage-m.com',
    '39*tech-camp.in',
    '40*hasegawa-heart.com',    
    '41*steakland.jp',
    '42*showroomprive.com',
    '43*imas-cg.net',
    '44*filetender.com',
    '45*hexo.io',
    '46*yinwang.org',
    '47*blog.yitianshijie.net',
    '48*yatani.jp',
    '49*qiita.com',
    '50*52nlp.cn',
    '51*guidetojapanese.org',
    '52*olderadults.mobi',
    '53*blog.whatsapp.com',
    '54*tech-jp.co.jp',
    '56*sankei.com',
    '55*lomake.fi',
    '57*bgmaimuna.com',
    '58*0dt.net',
    '59*web.ics.purdue.edu',
    '60*canon-foundation.jp',
    '61*tech.nikkeibp.co.jp',
    '62*jp.techcrunch.com',
    '63*capcom.co.jp',
    '64*blog.sciencenet.cn',
    '65*pantone.com',
    '66*cerezo.jp',
    '67*news.livedoor.com',

    # One more overlap, delete
    '68*360.cn',

    '69*tokai-tv.com', 
    '70*life-is-tech.com',
    '71*bloomberg.co.jp',
    '72*boagworld.com',
    '73*designmodo.com',
    '74*forbesjapan.com',
    '75*guzen.biz',
    '76*hatenablog.jp',
    '77*ikedahayato.com',
    '78*kochi-arindo.com',
    '79*lamp-guesthouse.com',
    '80*liginc.co.jp',
    '81*usabilitygeek.com',
    '82*yoichiochiai.com',
    '83*zeyo.jp',
    '84*berg.jp',
    '85*billysbakerynyc.com',
    '86*buenosairesbakery.com.ar',
    '87*cafe-sanctuary.jp',
    '88*flanet.web.fc2.com',
    '89*fmltd.co.jp',

    # can not show, delete
    #'90*hanakinoboru.com.png',
    '90*security.ec-current.com',

    '91*heidicohen.com',
    '92*ironwork.jp',
    '93*jimmakos.com',
    '94*keycoffee.co.jp',
    '95*shimomaruko-ikkyu.com',
    '96*thehairypotato.co',
    '97*towafood-net.co.jp',
    '98*americanfruitandproduce.com',
    '99*frenchbakerynj.com',
    '100*ren-shinjuku.com',
    '101*econlib.org',
    '102*nateas.com',
    '103*kurose.co.jp',
    '104*sonic1.co.jp',
    '105*sundaico.co.jp',
    '106*ren-shinjuku.com',
    '107*art-sys.co.jp',
    '108*kasinoki.co.jp',
    '109*nagainori.co.jp',
    '110*yamasakigiken.co.jp',
    '111*mozilla.org',
    '112*booth.pm.ja',
    '113*chifure.co.jp',
    '114*fantia.jp',
    '115*freebiesbug.com',
    '116*galaxymobile.jp',

    '117*gmo.jp',

    '118*icotto.jp',
    '119*inakami.net',
    '120*maybelline.co.jp',
    '121*oiax.jp',
    '122*paiza.jp',
    '123*railstutorial.jp',
    '124*saruwakakun.com',
    '125*sejuku.net',
    '126*skima.jp',
    '127*yuchrszk.blogspot.com',
    '128*yumeno.jp',
    '129*superprof.fr',
    '130*nounplus.net',
    '131*hdpfans.com',
    '132*ho-ginza.net',
    '133*sekimoto.dental',
    '134*coming-saji.com',
    '135*stratechery.com',
    '136*theclinic.cl',
    '137*interaction-design.org',
    '138*jlpt.jp',
    '139*kenkun-jinja.org',
    '140*ubejinja.or.jp',
    '141*jiankang.com',
    '142*hea.cn',
    '143*jfc.or.jp',
    '144*kudago.com',
    '145*coolmath.com',
    '146*solvemymath.com',
    '147*mathleague.com',
    '148*math.com',
    '149*mathplayground.com',

    # Ayumu's Chinese & Japanese Webpage
    '150*bilibili.com',
    '151*nicovideo.jp',

    '152*rakuten.co.jp',
    '153*taobao.com',

    '154*ihotwind.cn',
    '155*uniqlo.com.jp',

    '156*dianping.com',
    '157*tabelog.com',

    '158*sina.com.cn',
    '159*yahoo.co.jp',

    '160*1688.com',
    '161*netsea.jp',

    '162*bj.ganji.com',
    '163*sumaity.com',

    '164*estar.jp',
    '165*hongxiu.com',

    '166*tapple.me',
    '167*baihe.com'

    #'168*360.cn',->68
    #'169*security.ec-current.com'->90
]



# WebpageList = [

#     '0*19lou.com_h1_1',
#     '1*19lou.com_v1_1',
#     '2*19lou.com',
#     '3*1688.com_h1_1',
#     '4*1688.com_v1_1',
#     '5*1688.com',
#     '6*art-sys.co.jp_h1_1',
#     '7*art-sys.co.jp',
#     '8*bilibili.com_h1_1',
#     '9*bilibili.com_v1_1',
#     '10*bilibili.com',
#     '11*blog.sciencenet.cn_h1_1',
#     '12*blog.sciencenet.cn_v1_1',
#     '13*blog.sciencenet.cn',
#     '14*bloomberg.co.jp_h1_1',
#     '15*bloomberg.co.jp_v1_1',
#     '16*bloomberg.co.jp',
#     '17*boagworld.com_h1_1',
#     '18*boagworld.com_v1_1',
#     '19*boagworld.com',
#     '20*bootcdn.cn_h1_1',
#     '21*bootcdn.cn_v1_1',
#     '22*bootcdn.cn',
#     '23*booth.pm.ja_h1_1',
#     '24*booth.pm.ja_v1_1',
#     '25*booth.pm.ja',
#     '26*buenosairesbakery.com.ar_h1_1',
#     '27*buenosairesbakery.com.ar',
#     '28*cafe-sanctuary.jp_h1_1',
#     '29*cafe-sanctuary.jp_v1_1',
#     '30*cafe-sanctuary.jp',
#     '31*canon-foundation.jp_h1_1',
#     '32*canon-foundation.jp',
#     '33*capcom.co.jp_h1_1',
#     '34*capcom.co.jp_v1_1',
#     '35*capcom.co.jp',
#     '36*cheshi.com_h1_1',
#     '37*cheshi.com_v1_1',
#     '38*cheshi.com',
#     '39*chi2019.acm.org_v1_1',
#     '40*chi2019.acm.org',
#     '41*clamav.net_h1_1',
#     '42*clamav.net',
#     '43*coming-saji.com_h1_1',
#     '44*coming-saji.com_v1_1',
#     '45*coming-saji.com',
#     '46*coolmath.com_h1_1',
#     '47*coolmath.com_v1_1',
#     '48*coolmath.com',
#     '49*cp.pocky.jp_h1_1',
#     '50*cp.pocky.jp',
#     '51*cps.com.cn_h1_1',
#     '52*cps.com.cn',
#     '53*cvpr2018.thecvf.com_h1_1',
#     '54*cvpr2018.thecvf.com_v1_1',
#     '55*cvpr2018.thecvf.com',
#     '56*designmodo.com_h1_1',
#     '57*designmodo.com_v1_1',
#     '58*designmodo.com',
#     '59*designstub.com_h1_1',
#     '60*designstub.com_v1_1',
#     '61*designstub.com',
#     '62*dianping.com_h1_1',
#     '63*dianping.com_v1_1',
#     '64*dianping.com',
#     '65*disney.co.jp_h1_1',
#     '66*disney.co.jp',
#     '67*docs.opencv.org_v1_1',
#     '68*docs.opencv.org',
#     '69*econlib.org_h1_1',
#     '70*econlib.org_v1_1',
#     '71*econlib.org',
#     '72*estar.jp_h1_1',
#     '73*estar.jp',
#     '74*estar.jp_v1_1',
#     '75*fmltd.co.jp_h1_1',
#     '76*fmltd.co.jp_v1_1',
#     '77*fmltd.co.jp',
#     '78*forbesjapan.com_h1_1',
#     '79*forbesjapan.com_v1_1',
#     '80*forbesjapan.com',
#     '81*hanakinoboru.com_h1_1',
#     '82*hanakinoboru.com_v1_1',
#     '83*hanakinoboru.com',
#     '84*hasegawa-heart.com_h1_1',
#     '85*hasegawa-heart.com_v1_1',
#     '86*hasegawa-heart.com',
#     '87*hdpfans.com_h1_1',
#     '88*hdpfans.com_v1_1',
#     '89*hdpfans.com',
#     '90*hea.cn_v1_1',
#     '91*hea.cn',
#     '92*hongxiu.com_h1_1',
#     '93*hongxiu.com_v1_1',
#     '94*hongxiu.com',
#     '95*huxiu.com_h1_1',
#     '96*huxiu.com_v1_1',
#     '97*huxiu.com',
#     '98*icotto.jp_h1_1',
#     '99*icotto.jp_v1_1',
#     '100*icotto.jp'
# ]
