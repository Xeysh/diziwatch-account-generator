(()=>{"use strict";function t(t){const e=t.dataset.button,s=document.getElementsByClassName("tab-content");for(let t=0;t<s.length;t++)s[t].style.display="none";const a=document.getElementsByClassName("tab-button");for(let t=0;t<a.length;t++)a[t].style.backgroundColor="";document.querySelector(`[data-tab="${e}"]`).style.display="block",t.classList.add("active");for(let e=0;e<a.length;e++)a[e]!==t&&a[e].classList.remove("active")}!function(){function e(){chrome.storage.local.get(["hcaptcha_auto_open","hcaptcha_auto_solve","hcaptcha_click_delay_time","hcaptcha_solve_delay_time","recaptcha_auto_open","recaptcha_auto_solve","recaptcha_click_delay_time","recaptcha_solve_delay_time"],(async t=>{const e=document.getElementsByClassName("settings_toggle"),s=document.getElementsByClassName("settings_text");for(const s of e)s.classList.remove("on","off"),s.classList.add(t[s.dataset.settings]?"on":"off");for(const e of s)e.value=t[e.dataset.settings]}));const e=async t=>{var e=t.classList.contains("settings_toggle")?t.classList.contains("off"):t.value;await chrome.storage.local.set({[t.dataset.settings]:e}),t.classList.contains("settings_toggle")&&(t.classList.remove("on","off"),t.classList.add(e?"on":"off"))};for(const t of document.querySelectorAll(".settings_toggle, .settings_text"))t.classList.contains("settings_toggle")?t.addEventListener("click",(()=>e(t))):t.classList.contains("settings_text")&&t.addEventListener("input",(()=>e(t)));const s=document.getElementsByClassName("tab-button");for(let e=0;e<s.length;e++)s[e].addEventListener("click",(()=>t(s[e])));document.querySelector(".tab-button").click()}document.addEventListener("DOMContentLoaded",e)}()})();