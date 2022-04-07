const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
const resvYear = document.querySelector('.resv-year');
const resvMonth = document.querySelector('.resv-month');
const resvDay = document.querySelector('.resv-day');

exitBtn.addEventListener('click', ()=>{resvTab.classList.remove('open');});


// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []
const dateFunc = ()=>{
    const dates = document.querySelectorAll('.date');
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    dates.forEach((i)=>{
        i.addEventListener('click', ()=>{
            resvYear.textContent = year.textContent;
            resvMonth.textContent=month.textContent;
            resvDay.textContent= i.textContent.split('EVENT')[0];
            /////////////////////////////////////////////////////////////
            var y = year.textContent;
            var m = month.textContent;
            var d = i.textContent.split('EVENT')[0].trim();
            if(m.length != 2){
                m = '0' + m;
            }
            if(d.length != 2){
                d = '0' + d;
            }
            document.getElementById("onlydatetime").value = y + '-' + m + '-' + d;
            ListCal();
            /////////////////////////////////////////////////////////////
            if(i.classList.contains('other') || i.classList.contains('selected')){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                i.classList.remove('selected');
                selDate.length=0;
            }else if(selDate.length > 0){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                selDate.length=0;
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
            }else{
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');

            }
        });
    });
};

// 초기화 함수
const reset = ()=>{
    selDate.length=0;
    dateFunc();
}

// 로드시 Nav 버튼들 이벤트 등록 및 초기화
window.onload=()=>{
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf=>{
        if(inf.classList.contains('go-prev')){
            inf.addEventListener('click', ()=>{prevMonth(); reset();});
        }else if(inf.classList.contains('go-today')){
            inf.addEventListener('click', ()=>{goToday(); reset();});
        }else if(inf.classList.contains('go-next')){
            inf.addEventListener('click', ()=>{nextMonth(); reset();});
        }
    });
    reset();
}