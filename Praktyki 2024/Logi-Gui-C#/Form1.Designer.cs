﻿namespace Logi_Gui
{
    partial class Form1
    {
        /// <summary>
        /// Wymagana zmienna projektanta.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Wyczyść wszystkie używane zasoby.
        /// </summary>
        /// <param name="disposing">prawda, jeżeli zarządzane zasoby powinny zostać zlikwidowane; Fałsz w przeciwnym wypadku.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Kod generowany przez Projektanta formularzy systemu Windows

        /// <summary>
        /// Metoda wymagana do obsługi projektanta — nie należy modyfikować
        /// jej zawartości w edytorze kodu.
        /// </summary>
        private void InitializeComponent()
        {
            this.lista = new System.Windows.Forms.ListView();
            this.k1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.k2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.k3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.k4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.k5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.k6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.load_button = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lista
            // 
            this.lista.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.k1,
            this.k2,
            this.k3,
            this.k4,
            this.k5,
            this.k6});
            this.lista.HideSelection = false;
            this.lista.Location = new System.Drawing.Point(12, 12);
            this.lista.Name = "lista";
            this.lista.Size = new System.Drawing.Size(1232, 371);
            this.lista.TabIndex = 0;
            this.lista.UseCompatibleStateImageBehavior = false;
            this.lista.View = System.Windows.Forms.View.Details;
            // 
            // k1
            // 
            this.k1.Text = "IP";
            this.k1.Width = 257;
            // 
            // k2
            // 
            this.k2.Text = "Kod";
            this.k2.Width = 220;
            // 
            // k3
            // 
            this.k3.Text = "Indeks";
            this.k3.Width = 186;
            // 
            // k4
            // 
            this.k4.Text = "data";
            this.k4.Width = 187;
            // 
            // k5
            // 
            this.k5.Text = "Nazwa";
            this.k5.Width = 226;
            // 
            // k6
            // 
            this.k6.Text = "Czy jest błędne";
            this.k6.Width = 133;
            // 
            // load_button
            // 
            this.load_button.Location = new System.Drawing.Point(611, 389);
            this.load_button.Name = "load_button";
            this.load_button.Size = new System.Drawing.Size(75, 23);
            this.load_button.TabIndex = 1;
            this.load_button.Text = "Załaduj";
            this.load_button.UseVisualStyleBackColor = true;
            this.load_button.Click += new System.EventHandler(this.load_button_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1256, 450);
            this.Controls.Add(this.load_button);
            this.Controls.Add(this.lista);
            this.Name = "Form1";
            this.Text = "Gui-logi";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView lista;
        private System.Windows.Forms.ColumnHeader k1;
        private System.Windows.Forms.ColumnHeader k2;
        private System.Windows.Forms.ColumnHeader k3;
        private System.Windows.Forms.Button load_button;
        private System.Windows.Forms.ColumnHeader k4;
        private System.Windows.Forms.ColumnHeader k5;
        private System.Windows.Forms.ColumnHeader k6;
    }
}
