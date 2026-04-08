# ==============================================================================
# Plot efg_rate - three_pt_rate: tirare tante triple garantisce un'efficienza più alta?
# ==============================================================================

# Y: Efficienza Realizzativa Effettiva
Y_efficiency = df_game_clear['efg_pct'].values

# # Regressione lineare: coefs_eff = [pendenza_eff (m), intercetta_eff (q)]
# coefs_2 = np.polyfit(X_volume, Y_efficiency, 1)
# trend_eff_function = np.poly1d(coefs_2)

r2, p_value2 = stats.spearmanr(X_volume, Y_efficiency)
print("efg_rate - three_pt_rate: ",r2, p_value2)

#--- Scatter Plot 2---
scatter = ax2.scatter(
  X_volume,                    # Asse X: Volume tiri da 3
  Y_efficiency,                # Asse Y: Efficienza Effettiva (eFG%)
  c=df_game_clear['season'],   # Colore basato sull'anno (per vedere la transizione)
  cmap='viridis',              # Palette: viola (vecchio) -> giallo (nuovo)
  alpha=0.6,                   # Trasparenza per gestire la sovrapposizione
  edgecolor='none'             # Rimuove il bordo dei punti per pulizia
)


# Usiamo i valori minimi e massimi osservati di X per definire gli estremi della linea
X_eff_range = np.array([X_volume.min(), X_volume.max()])
ax2.plot(
  X_eff_range,
  trend_eff_function(X_eff_range),
  color='red', linestyle='--',
  label=f'y={coefs_2[0]:.2f}x + {coefs_2[1]:.2f}'
)

ax2.set_xlabel('Tiri da 3 (%)')
ax2.set_ylabel('eFG%')

# Vincoliamo gli assi in modo realistico (le percentuali sono tra 0 e 1)
# Un eFG% < 30% o > 70% è quasi impossibile a livello stagionale per un team
#ax2.set_ylim(0, 1)
ax2.grid(True, linestyle=':', alpha=0.5)
#ax2.legend(loc='upper left')


# ==============================================================================
# win_rate - fg_rate: L'efficienza classica è ciò che correla maggiormente con le vittorie?
# ==============================================================================

# # X: Efficienza, Y: Vittorie
# X_fg = df_game_clear['fg_pct'].values

# r4, p_value4 = stats.spearmanr(X_fg, Y_win)
# print("win_rate - fg_rate: ",r4, p_value4)

# scatter4 = ax4.scatter(
#   X_fg, 
#   Y_win, 
#   c=df_game_clear['season'], 
#   cmap='viridis',
#   alpha=0.6, 
#   edgecolor='none'
# )

# ax4.set_xlabel('FG%')
# ax4.set_ylabel('Win (%)')
# #ax4.set_ylim(0, 1)
# ax4.grid(True, linestyle=':', alpha=0.5)