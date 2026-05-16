'use client';

import { useSimulation } from "@/lib/simulation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { AlertCircle, Battery, BatteryCharging, Crosshair, Map as MapIcon, CheckCircle2 } from "lucide-react";
import dynamic from 'next/dynamic';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const FieldMap = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <div className="h-full w-full bg-muted flex items-center justify-center animate-pulse rounded-xl">Loading Live Map...</div> });

const mockChartData = [
  { time: '08:00', water: 120 },
  { time: '09:00', water: 135 },
  { time: '10:00', water: 190 },
  { time: '11:00', water: 220 },
  { time: '12:00', water: 280 },
  { time: '13:00', water: 340 },
];

export default function DashboardPage() {
  const { drones, rover, detections, tasks, stats, approveTask } = useSimulation();

  return (
    <div className="container py-8 flex flex-col gap-8 relative z-10">
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">Reddy Farms — Hyderabad, Telangana</h1>
          <p className="text-text-secondary text-lg mt-1">Farmer Command Center</p>
        </div>
        <Badge variant="outline" className="border-accent-green text-accent-green px-4 py-1.5 text-sm bg-accent-green/5 shadow-sm">
          <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> System Active
        </Badge>
      </div>

      {/* STATS ROW */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Acres Scanned</CardTitle>
            <MapIcon className="h-5 w-5 text-text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{stats.acresScanned}</div>
            <p className="text-sm text-accent-green mt-1 font-medium">↑ +2.1 this hour</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Detections</CardTitle>
            <AlertCircle className="h-5 w-5 text-alert-red" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-alert-red">{detections.filter(d => d.disease !== 'Healthy').length}</div>
            <p className="text-sm text-text-secondary mt-1">Needs review</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Fleet</CardTitle>
            <Crosshair className="h-5 w-5 text-accent-green" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{drones.length}/3 Drones</div>
            <p className="text-sm text-text-secondary mt-1">1 Rover active</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 border-b-4 border-b-blue-500">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Water Saved</CardTitle>
            <CheckCircle2 className="h-5 w-5 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{stats.waterSaved}L</div>
            <p className="text-sm text-text-secondary mt-1">Today vs Flood Irrigation</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* MAP & CHART */}
        <div className="lg:col-span-2 flex flex-col gap-8">
          <div className="h-[450px] rounded-xl overflow-hidden border border-border shadow-xl glass-card">
            <FieldMap />
          </div>

          <Card className="glass-card">
            <CardHeader>
              <CardTitle>Water Savings Trend (Liters)</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="h-[250px] w-full min-h-[250px] min-w-0">
                <ResponsiveContainer width="100%" height="100%" minHeight={200} minWidth={200}>
                  <AreaChart data={mockChartData}>
                    <defs>
                      <linearGradient id="colorWater" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="hsl(var(--border))" />
                    <XAxis dataKey="time" stroke="hsl(var(--text-muted))" fontSize={12} tickLine={false} axisLine={false} />
                    <YAxis stroke="hsl(var(--text-muted))" fontSize={12} tickLine={false} axisLine={false} />
                    <Tooltip contentStyle={{ backgroundColor: 'hsl(var(--card))', border: '1px solid hsl(var(--border))', borderRadius: '8px' }} />
                    <Area type="monotone" dataKey="water" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorWater)" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* SIDEBAR */}
        <div className="flex flex-col gap-8">

          {/* FLEET STATUS */}
          <Card className="glass-card">
            <CardHeader className="pb-4">
              <CardTitle className="text-lg">Fleet Telemetry</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              {drones.map(d => (
                <div key={d.id} className="flex items-center justify-between text-sm group">
                  <div className="flex items-center gap-3">
                    <span className="font-bold w-8 text-foreground">{d.id}</span>
                    <Battery className={`w-4 h-4 ${d.battery < 70 ? 'text-alert-amber' : 'text-accent-green'}`} />
                    <div className="w-24 h-2 bg-muted rounded-full overflow-hidden">
                      <div className={`h-full ${d.battery < 70 ? 'bg-alert-amber' : 'bg-accent-green'}`} style={{ width: `${d.battery}%` }}></div>
                    </div>
                  </div>
                  <Badge variant={d.status === 'Returning' ? 'secondary' : 'default'} className="w-24 justify-center text-[10px] uppercase font-bold tracking-wider">
                    {d.status}
                  </Badge>
                </div>
              ))}
              <div className="h-px bg-border my-4"></div>
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-3">
                  <span className="font-bold w-8 text-foreground">{rover.id}</span>
                  <BatteryCharging className="w-4 h-4 text-blue-500" />
                  <div className="w-24 h-2 bg-muted rounded-full overflow-hidden">
                    <div className="h-full bg-blue-500" style={{ width: `${rover.battery}%` }}></div>
                  </div>
                </div>
                <Badge variant={rover.status === 'Idle' ? 'secondary' : 'default'} className="w-24 justify-center bg-blue-600 text-white hover:bg-blue-700 text-[10px] uppercase font-bold tracking-wider shadow-md">
                  {rover.status}
                </Badge>
              </div>
            </CardContent>
          </Card>

          {/* TASKS */}
          <Card className="flex-1 flex flex-col overflow-hidden glass-card">
            <CardHeader className="pb-4 border-b border-border bg-background/30">
              <CardTitle className="text-lg">Task Console</CardTitle>
            </CardHeader>
            <CardContent className="p-0 flex-1 overflow-auto">
              <Tabs defaultValue="pending" className="w-full h-full flex flex-col">
                <div className="px-4 py-3 bg-background/50 border-b border-border">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="pending">Pending ({tasks.filter(t => t.status === 'Pending').length})</TabsTrigger>
                    <TabsTrigger value="active">Active ({tasks.filter(t => t.status === 'In Progress').length})</TabsTrigger>
                  </TabsList>
                </div>
                <TabsContent value="pending" className="p-5 m-0 flex-1 overflow-auto space-y-4">
                  {tasks.filter(t => t.status === 'Pending').map(t => (
                    <div key={t.id} className="p-4 rounded-xl bg-background border border-border shadow-sm hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <h4 className="font-semibold text-sm text-foreground">{t.title}</h4>
                        <Badge variant="destructive" className="bg-alert-red/10 text-alert-red border-alert-red/20 text-[10px] font-bold">
                          {t.priority}
                        </Badge>
                      </div>
                      <p className="text-xs text-text-secondary mb-4 flex items-center gap-1 font-medium">
                        <MapIcon className="w-3 h-3" /> Target Zone {t.zone}
                      </p>
                      <Button size="sm" className="w-full bg-accent-green text-white hover:bg-emerald-600 shadow-md font-semibold" onClick={() => approveTask(t.id)}>
                        Approve & Dispatch Rover
                      </Button>
                    </div>
                  ))}
                  {tasks.filter(t => t.status === 'Pending').length === 0 && (
                    <div className="text-center text-text-muted text-sm py-12 flex flex-col items-center">
                      <CheckCircle2 className="w-8 h-8 text-border mb-3" />
                      All clear! No pending tasks.
                    </div>
                  )}
                </TabsContent>
                <TabsContent value="active" className="p-5 m-0 space-y-4">
                  {tasks.filter(t => t.status === 'In Progress').map(t => (
                    <div key={t.id} className="p-4 rounded-xl bg-background border border-border shadow-sm border-l-4 border-l-blue-500 relative overflow-hidden">
                      <div className="absolute top-0 right-0 w-16 h-16 bg-blue-500/10 rounded-bl-full pointer-events-none"></div>
                      <h4 className="font-semibold text-sm text-foreground mb-1">{t.title}</h4>
                      <p className="text-xs text-text-secondary font-medium">Executing in Zone {t.zone}</p>
                    </div>
                  ))}
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}