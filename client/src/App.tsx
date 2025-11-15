import { AppProvider, useApp } from './contexts/AppContext';
import { Sidebar } from './components/Sidebar';
import { Dashboard } from './components/Dashboard';
import { TradeRegistration } from './components/TradeRegistration';

function AppContent() {
  const { currentScreen } = useApp();

  return (
    <div className="min-h-screen bg-slate-50 flex">
      <Sidebar />
      <main className="flex-1 overflow-auto">
        {currentScreen === 'dashboard' && <Dashboard />}
        {currentScreen === 'register' && <TradeRegistration />}
      </main>
    </div>
  );
}

function App() {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
}

export default App;
