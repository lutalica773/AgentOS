from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from core.prime_agent import PrimeAgent
from core.agent_store import AgentStore
from core.memory import Memory

app = FastAPI()

prime = PrimeAgent()
store = AgentStore()
memory = Memory()


@app.get("/")
def root():
    return {"AgentOS": "running"}


    @app.post("/intent")
    def handle_intent(intent: str):
        result = prime.route_intent(intent)
            return {"result": result}


            @app.post("/install")
            def install(name: str, purpose: str):
                return {"status": store.install_agent(name, purpose)}


                @app.get("/dashboard", response_class=HTMLResponse)
                def dashboard():

                    history = memory.history()
                        stats = memory.get_stats()

                            html = f"""
                                <html>
                                    <head>
                                            <title>AgentOS Dashboard</title>
                                                </head>
                                                    <body style="font-family: Arial; background:#111; color:white; padding:20px">

                                                            <h1>🧠 AgentOS Control Center</h1>

                                                                    <h2>Most Used Intents</h2>
                                                                            <pre>{stats}</pre>

                                                                                    <h2>Intent History</h2>
                                                                                            <pre>{history[-10:]}</pre>

                                                                                                </body>
                                                                                                    </html>
                                                                                                        """

                                                                                                            return html