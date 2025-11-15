import { useState, useRef, useEffect } from 'react';
import { Upload, Image as ImageIcon, X, CheckCircle, AlertCircle, Clipboard } from 'lucide-react';
import { api } from '../services/api';

export function TradeRegistration() {
  const [formData, setFormData] = useState({
    asset: '',
    type: 'BUY' as 'BUY' | 'SELL',
    category: 'CRYPTO' as 'CRYPTO' | 'STOCKS' | 'FOREX' | 'DERIVATIVES',
    quantity: '',
    entry_price: '',
    exit_price: '',
    stop_loss: '',
    take_profit: '',
    status: 'OPEN' as 'OPEN' | 'CLOSED' | 'PENDING',
    notes: '',
  });

  const [screenshot, setScreenshot] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const handlePaste = (e: ClipboardEvent) => {
      const items = e.clipboardData?.items;
      if (!items) return;

      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
          const blob = items[i].getAsFile();
          if (blob) {
            handleImageFile(blob);
          }
        }
      }
    };

    window.addEventListener('paste', handlePaste);
    return () => window.removeEventListener('paste', handlePaste);
  }, []);

  const handleImageFile = (file: File) => {
    setScreenshot(file);
    const url = URL.createObjectURL(file);
    setPreviewUrl(url);
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      handleImageFile(file);
    }
  };

  const removeScreenshot = () => {
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }
    setScreenshot(null);
    setPreviewUrl(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      const formDataToSend = new FormData();

      formDataToSend.append('asset', formData.asset);
      formDataToSend.append('type', formData.type);
      formDataToSend.append('category', formData.category);
      formDataToSend.append('quantity', formData.quantity);
      formDataToSend.append('entry_price', formData.entry_price);
      formDataToSend.append('status', formData.status);

      if (formData.exit_price) formDataToSend.append('exit_price', formData.exit_price);
      if (formData.stop_loss) formDataToSend.append('stop_loss', formData.stop_loss);
      if (formData.take_profit) formDataToSend.append('take_profit', formData.take_profit);
      if (formData.notes) formDataToSend.append('notes', formData.notes);
      if (screenshot) formDataToSend.append('screenshot', screenshot);

      await api.createTrade(formDataToSend);

      setSuccess(true);
      setFormData({
        asset: '',
        type: 'BUY',
        category: 'CRYPTO',
        quantity: '',
        entry_price: '',
        exit_price: '',
        stop_loss: '',
        take_profit: '',
        status: 'OPEN',
        notes: '',
      });
      removeScreenshot();

      setTimeout(() => setSuccess(false), 3000);
    } catch (err) {
      setError('Erro ao registrar operação. Verifique a conexão com o backend.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="p-8 max-w-4xl mx-auto">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-slate-800 mb-2">Nova Operação</h2>
        <p className="text-slate-600">Registre uma nova operação de trading</p>
      </div>

      {success && (
        <div className="mb-6 p-4 bg-emerald-50 border border-emerald-200 rounded-lg flex items-center gap-3">
          <CheckCircle className="w-5 h-5 text-emerald-600" />
          <p className="text-emerald-800 font-medium">Operação registrada com sucesso!</p>
        </div>
      )}

      {error && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg flex items-center gap-3">
          <AlertCircle className="w-5 h-5 text-red-600" />
          <p className="text-red-800">{error}</p>
        </div>
      )}

      <form onSubmit={handleSubmit} className="bg-white rounded-xl shadow-sm border border-slate-200 p-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Ativo <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="asset"
              value={formData.asset}
              onChange={handleChange}
              required
              placeholder="Ex: BTCUSDT, AAPL, EURUSD"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Tipo <span className="text-red-500">*</span>
            </label>
            <select
              name="type"
              value={formData.type}
              onChange={handleChange}
              required
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            >
              <option value="BUY">Compra (Long)</option>
              <option value="SELL">Venda (Short)</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Categoria <span className="text-red-500">*</span>
            </label>
            <select
              name="category"
              value={formData.category}
              onChange={handleChange}
              required
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            >
              <option value="CRYPTO">Criptomoedas</option>
              <option value="STOCKS">Ações</option>
              <option value="FOREX">Forex</option>
              <option value="DERIVATIVES">Derivativos</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Status <span className="text-red-500">*</span>
            </label>
            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              required
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            >
              <option value="OPEN">Aberta</option>
              <option value="CLOSED">Fechada</option>
              <option value="PENDING">Pendente</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Quantidade <span className="text-red-500">*</span>
            </label>
            <input
              type="number"
              name="quantity"
              value={formData.quantity}
              onChange={handleChange}
              required
              step="any"
              placeholder="0.00"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Preço de Entrada <span className="text-red-500">*</span>
            </label>
            <input
              type="number"
              name="entry_price"
              value={formData.entry_price}
              onChange={handleChange}
              required
              step="any"
              placeholder="0.00"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Preço de Saída
            </label>
            <input
              type="number"
              name="exit_price"
              value={formData.exit_price}
              onChange={handleChange}
              step="any"
              placeholder="0.00"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Stop Loss
            </label>
            <input
              type="number"
              name="stop_loss"
              value={formData.stop_loss}
              onChange={handleChange}
              step="any"
              placeholder="0.00"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-700 mb-2">
              Take Profit
            </label>
            <input
              type="number"
              name="take_profit"
              value={formData.take_profit}
              onChange={handleChange}
              step="any"
              placeholder="0.00"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
            />
          </div>
        </div>

        <div className="mb-6">
          <label className="block text-sm font-semibold text-slate-700 mb-2">
            Observações
          </label>
          <textarea
            name="notes"
            value={formData.notes}
            onChange={handleChange}
            rows={4}
            placeholder="Adicione notas sobre a operação, estratégia utilizada, etc..."
            className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent resize-none"
          />
        </div>

        <div className="mb-8">
          <label className="block text-sm font-semibold text-slate-700 mb-2">
            Screenshot da Operação
          </label>

          {!previewUrl ? (
            <div className="border-2 border-dashed border-slate-300 rounded-lg p-8">
              <div className="text-center">
                <div className="flex justify-center gap-4 mb-4">
                  <Upload className="w-12 h-12 text-slate-400" />
                  <Clipboard className="w-12 h-12 text-slate-400" />
                </div>
                <p className="text-slate-600 mb-2">
                  Arraste uma imagem aqui ou clique para selecionar
                </p>
                <p className="text-sm text-slate-500 mb-4">
                  Você também pode colar (Ctrl+V) uma imagem da área de transferência
                </p>
                <button
                  type="button"
                  onClick={() => fileInputRef.current?.click()}
                  className="px-4 py-2 bg-slate-100 text-slate-700 rounded-lg hover:bg-slate-200 transition-colors"
                >
                  Selecionar Arquivo
                </button>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="image/*"
                  onChange={handleFileSelect}
                  className="hidden"
                />
              </div>
            </div>
          ) : (
            <div className="relative border border-slate-300 rounded-lg overflow-hidden">
              <img src={previewUrl} alt="Preview" className="w-full h-auto" />
              <button
                type="button"
                onClick={removeScreenshot}
                className="absolute top-2 right-2 p-2 bg-red-500 text-white rounded-full hover:bg-red-600 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
              <div className="absolute bottom-2 left-2 px-3 py-1 bg-black/70 text-white text-sm rounded-lg flex items-center gap-2">
                <ImageIcon className="w-4 h-4" />
                {screenshot?.name || 'Imagem da área de transferência'}
              </div>
            </div>
          )}
        </div>

        <div className="flex gap-4">
          <button
            type="submit"
            disabled={loading}
            className="flex-1 px-6 py-3 bg-emerald-500 text-white font-semibold rounded-lg hover:bg-emerald-600 transition-colors disabled:bg-slate-300 disabled:cursor-not-allowed"
          >
            {loading ? 'Registrando...' : 'Registrar Operação'}
          </button>
          <button
            type="button"
            onClick={() => {
              setFormData({
                asset: '',
                type: 'BUY',
                category: 'CRYPTO',
                quantity: '',
                entry_price: '',
                exit_price: '',
                stop_loss: '',
                take_profit: '',
                status: 'OPEN',
                notes: '',
              });
              removeScreenshot();
            }}
            className="px-6 py-3 bg-slate-100 text-slate-700 font-semibold rounded-lg hover:bg-slate-200 transition-colors"
          >
            Limpar
          </button>
        </div>
      </form>
    </div>
  );
}
