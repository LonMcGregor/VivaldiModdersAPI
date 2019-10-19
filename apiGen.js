function generateVivaldiAPI(){
    let vapi = '';
    const doc = document.implementation.createHTMLDocument('Vivaldi API Reference');
    doc.body.insertAdjacentHTML('afterbegin', `<h1>Vivaldi Modders API Reference</h1>
    <button>Expand/Collapse all (for searching with ctrl+f)</button>
    <script type="text/javascript">
        document.querySelector("button").addEventListener("click", e => {
            const allDetails = Array.from(document.querySelectorAll("details"));
            e.target.className = e.target.className ==="open" ? "" : "open";
            allDetails.forEach(d => d.open = e.target.className);
        });
    </script>
    <details>
        <summary>
            <h2 id="listenerHelp">Listeners</h2>
        </summary>
        <p>Each listener method has the same functions, used for each listener API in the same way:</p>
        <div class="method">
            <h3>.addListener()</h3>
            <ul>
                <li><span class="type">function</span><span> </span><span class="name">listener</span></li>
            </ul>
            <p>Adds a function to a listener for an event</p>
        </div>
        <div class="method">
            <h3>.removeListener()</h3>
            <ul>
                <li><span class="type">function</span><span> </span><span class="name">listener</span></li>
            </ul>
            <p>Removes a function to a listener for an event</p>
        </div>
        <div class="method">
            <h3>.hasListener()</h3>
            <ul>
                <li><span class="type">function</span><span> </span><span class="name">listener</span></li>
            </ul>
            <p>Returns a boolean if a function is attached to a listener for an event</p>
        </div>
        <div class="method">
            <h3>.hasListeners()</h3>
            <p>Returns a boolean if a listener has any attached functions</p>
        </div>
        <div class="method">
            <h3>.dispatch()</h3>
            <p>Returns array of promises dispatched to the listener</p>
        </div>
    </details>`);
    Object.keys(vivaldi).forEach(api => {
        const detail = document.createElement('details');
        const summary = document.createElement('summary');
        summary.innerHTML = `<h2>${api}</h2>`;
        detail.appendChild(summary);
        Object.keys(vivaldi[api]).forEach(method => {
            vapi  += api + '.' + method + '\n';
            const description = doc.createElement('ul');
            let type;
            if(method.indexOf('on')===0){
                // Object.keys(vivaldi[api][method]).forEach(listener => {
                //     const li = document.createElement("li");
                //     li.innerText = listener;
                //     description.appendChild(li);
                // });
                type = 'listener';
            } else if (method.substr(0,1).match('[A-Z]')){
                Object.keys(vivaldi[api][method]).forEach(enumerated => {
                    const li = document.createElement('li');
                    li.innerText = enumerated;
                    description.appendChild(li);
                });
                type = 'enum';
            } else if (method === 'exit'){
                description.innerText = 'Quits Vivaldi';
                type = 'method';
            } else if (method === 'showPasswordDialog'){
                description.innerText = 'Invokes OS Password Authenticator';
                type = 'method';
            } else {
                try {
                    const result = vivaldi[api][method]();
                    const typeResult = typeof(result);
                    if(typeResult!=='undefined'){
                        const li = document.createElement('li');
                        li.innerText = 'Returns ' + typeResult;
                        description.appendChild(li);
                    } else {
                        const li = document.createElement('li');
                        li.innerText = 'Unknow arguments';
                        description.appendChild(li);
                    }
                } catch (e) {
                    let signature = e.message.replace('Error in invocation of ', '');
                    signature = signature.replace(': No matching signature.', '');
                    signature = signature.replace(`${api}.${method}(`, '');
                    signature = signature.replace(')', '');
                    let methodArgs = signature.split(',');
                    methodArgs = methodArgs.map(x => x.trim());
                    methodArgs = methodArgs.map(x => x.split(' '));
                    methodArgs.forEach(typeAndName => {
                        const li = document.createElement('li');
                        const typeSpan = document.createElement('span');
                        const nameSpan = document.createElement('span');
                        const space = document.createElement('span');
                        space.innerText = ' ';
                        if(typeAndName[0]==='optional'){
                            typeSpan.className = 'type';
                            typeSpan.innerText = typeAndName[0] + ' ' + typeAndName[1];
                            nameSpan.className = 'name';
                            nameSpan.innerText = typeAndName[2];
                        } else {
                            typeSpan.className = 'type';
                            typeSpan.innerText = typeAndName[0];
                            nameSpan.className = 'name';
                            nameSpan.innerText = typeAndName[1];
                        }
                        li.appendChild(typeSpan);
                        li.appendChild(space);
                        li.appendChild(nameSpan);
                        description.appendChild(li);
                    });
                }
                type = 'method';
            }
            const div = doc.createElement('div');
            div.className = type;
            const h = doc.createElement('h3');
            h.innerText = `vivaldi.${api}.${method}`;
            if(type==='method'){
                h.innerText = h.innerText + '()';
            }
            div.appendChild(h);
            div.appendChild(description);
            detail.appendChild(div);
        });
        doc.body.appendChild(detail);
    });
    //console.log(vapi);
    const htmldoc = `<html>
    <head>
    <style type="text/css">
        * {
            font-family: sans-serif
        }
        h1, h2, h3 {
            display: inline-block;
        }
        h3 {
            margin: auto;
        }
        details, details div {
            margin-left: 4px;
            border-left: 4px solid #ccc;
            padding-left: 4px;
        }
        details:hover, details div:hover {
            border-left-color: #999;
        }
        .type {
            color: blue;
            font-family: monospace;
        }
        .listener:before {
            content: '📣 Listener';
            background: green;
            color: white;
            padding: 4px;
            border-radius: 4px;
            margin-right: 4px;
        }
        .enum:before {
            content: '🚥 Enum';
            background: yellow;
            color: black;
            padding: 4px;
            border-radius: 4px;
            margin-right: 4px;
        }
    </style>
    <meta charset="utf-8" />
    <title>${doc.title}</title>
    </head>
    ${doc.body.outerHTML}
    </html>`;
    const htmlfile = new File(
        [htmldoc],
        'VivaldiAPIRef.html',
        {type: 'text/html'}
    );
    const htmlObjUrl = window.URL.createObjectURL(htmlfile);
    //chrome.tabs.create({url: htmlObjUrl});
    //document.querySelector("webview").src = htmlObjUrl;
    console.log(htmldoc);
}

generateVivaldiAPI();
