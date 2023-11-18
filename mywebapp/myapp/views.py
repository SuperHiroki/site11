from django.shortcuts import render

# Create your views here.

def base(request):
    context={
        'hamonuedaimei':'ベース',
        'hamonuedaimeisita':'???',
    }
    return render(request, 'app/base.html',context)

def home(request):
    context={
        'hamonuedaimei':'サイト説明',
        'hamonuedaimeisita':'作成日, 参考文献, etc.',
        'mokujione':'このサイトの使い方',
        'mokujitwo':'作成者, 作成日',
        'mokujithree':'参考文献',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/home.html',context)

def bunpunotokuchou(request):
    context={
        'hamonuedaimei':'分布の特徴',
        'hamonuedaimeisita':'分散, 標準偏差, etc',
        'mokujione':'平均, 分散, 標準偏差',
        'mokujitwo':'偏差値',
        'mokujithree':'歪度, 尖度',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/bunpunotokuchou.html',context)

def hubyoudoudo(request):
    context={
        'hamonuedaimei':'不平等度',
        'hamonuedaimeisita':'ローレンツ曲線, ジニ係数, etc',
        'mokujione':'度数分布の平均',
        'mokujitwo':'度数分布の分散',
        'mokujithree':'ジニ係数',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/hubyoudoudo.html',context)

def nihensuunokankei(request):
    context={
        'hamonuedaimei':'二変数の関係',
        'hamonuedaimeisita':'共分散, 相関係数, 回帰, 残差, etc',
        'mokujione':'共分散, 相関係数',
        'mokujitwo':'スピアマンの順位相関係数',
        'mokujithree':'偏相関係数',
        'mokujifour':'分割表データの相関係数',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/nihensuunokankei.html',context)

def kakuritunokiso(request):
    context={
        'hamonuedaimei':'確率の基礎',
        'hamonuedaimeisita':'条件付き確率, etc',
        'mokujione':'条件付き確率',
        'mokujitwo':'事象の独立性',
        'mokujithree':'独立の検定(予習)',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/kakuritunokiso.html',context)

def kakuritubunputokitaichi(request):
    context={
        'hamonuedaimei':'確率分布と期待値',
        'hamonuedaimeisita':'離散確率変数(確率関数), 連続確立変数(確率密度関数), etc',
        'mokujione':'離散確率変数(確率関数)の期待値',
        'mokujitwo':'連続確立変数(確率密度関数)の期待値',
        'mokujithree':'離散確率変数(確率関数)と連続確立変数(確率密度関数)の分散',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/kakuritubunputokitaichi.html',context)

def yuumeinakakuritubunpu(request):
    context={
        'hamonuedaimei':'有名な確率分布',
        'hamonuedaimeisita':'ベルヌーイ分布, 二項分布, ポアソン分布, 正規分布, etc',
        'mokujione':'二項分布',
        'mokujitwo':'ポアソン分布',
        'mokujithree':'正規分布',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/yuumeinakakuritubunpu.html',context)

def tahensuunokakuritubunpu(request):
    context={
        'hamonuedaimei':'多変数の確率分布',
        'hamonuedaimeisita':'同時確率関数, 同時確率密度関数, 共分散, 相関係数, etc',
        'mokujione':'同時確率関数, 周辺確率関数',
        'mokujitwo':'共分散, 相関係数',
        'mokujithree':'独立性の検定(予習)',
        'mokujifour':'相関係数、相関係数',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/tahensuunokakuritubunpu.html',context)

def randamuhyouhonkaranosuisoku(request):
    context={
        'hamonuedaimei':'ランダム標本と標本分布',
        'hamonuedaimeisita':'中心極限定理, 不偏分散, t-分布, etc',
        'mokujione':'二項分布(ベルヌーイ分布)',
        'mokujitwo':'正規分布(復習)',
        'mokujithree':'正規分布',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/randamuhyouhonkaranosuisoku.html',context)

def suitei(request):
    context={
        'hamonuedaimei':'推定',
        'hamonuedaimeisita':'最尤推定量, 信頼区間, etc',
        'mokujione':'最尤推定量(二項分布)',
        'mokujitwo':'母集団の分散が既知の時信頼区間',
        'mokujithree':'ベルヌーイ分布の信頼区間',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/suitei.html',context)

def kasetukentei(request):
    context={
        'hamonuedaimei':'仮説検定',
        'hamonuedaimeisita':'両側(片側)検定, t-検定, etc',
        'mokujione':'分散が既知の時の正規母集団の検定',
        'mokujitwo':'ベルヌーイ分布の検定',
        'mokujithree':'カイ二乗分布',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/kasetukentei.html',context)

def kaikibunseki(request):
    context={
        'hamonuedaimei':'回帰分析',
        'hamonuedaimeisita':'???, ???, etc',
        'mokujione':'mokujione',
        'mokujitwo':'mokujitwo',
        'mokujithree':'mokujithree',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/kaikibunseki.html',context)

def keizaisyakaideitanotoukeibunseki(request):
    context={
        'hamonuedaimei':'経済/社会データの統計分析',
        'hamonuedaimeisita':'???, ???, etc',
        'mokujione':'mokujione',
        'mokujitwo':'mokujitwo',
        'mokujithree':'mokujithree',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/keizaisyakaideitanotoukeibunseki.html',context)

def jikeiretudeitanotoukeibunseki(request):
    context={
        'hamonuedaimei':'時系列データの統計分析',
        'hamonuedaimeisita':'???, ???, etc',
        'mokujione':'mokujione',
        'mokujitwo':'mokujitwo',
        'mokujithree':'mokujithree',
        'mokujifour':'mokujifour',
        'mokujifive':'mokujifive',
        'mokujisix':'mokujisix',
        'mokujiseven':'mokujiseven',
        'mokujieight':'mokujieight',
        'mokujinine':'mokujinine',
        'mokujiten':'mokujiten',
        'mokujieleven':'mokujieleven',
        'mokujitwelve':'mokujitwelve',
    }
    return render(request, 'app/jikeiretudeitanotoukeibunseki.html',context)

def jikken(request):
    return render(request, 'app/jikken.html',{})



