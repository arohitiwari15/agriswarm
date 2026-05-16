'use client';

import { useSimulation } from "@/lib/simulation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { AlertCircle, Battery, BatteryCharging, Crosshair, Map as MapIcon, CheckCircle2 } from "lucide-react";
import dynamic from 'next/dynamic';


const FieldMap = dynamic(() => import('@/components/Map'), { ssr: false });

export default function DashboardPage() {
  const { drones, rover, detections, tasks, stats, approveTask } = useSimulation();

  return (
    <div className="container py-8 h-[calc(100vh-4rem)] flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Reddy Farms — Hyderabad, Telangana</h1>
          <p className="text-text-secondary">Farmer Command Center</p>
        </div>
        <Badge variant="outline" className="border-accent-green text-accent-green px-4 py-1 text-sm bg-accent-green/10">
          <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> System Active
        </Badge>
      </div>

      {/* STATS ROW */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Acres Scanned</CardTitle>
            <MapIcon className="h-4 w-4 text-text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.acresScanned}</div>
            <p className="text-xs text-accent-green">↑ +2.1 this hour</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Detections</CardTitle>
            <AlertCircle className="h-4 w-4 text-alert-red" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-alert-red">{detections.filter(d => d.disease !== 'Healthy').length}</div>
            <p className="text-xs text-text-secondary">Needs review</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Fleet</CardTitle>
            <Crosshair className="h-4 w-4 text-accent-green" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{drones.length}/3 Drones</div>
            <p className="text-xs text-text-secondary">1 Rover active</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Water Saved</CardTitle>
            <CheckCircle2 className="h-4 w-4 text-blue-400" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.waterSaved}L</div>
            <p className="text-xs text-text-secondary">Today vs Flood</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-[400px]">
        {/* MAP */}
        <div className="lg:col-span-2 h-full flex flex-col">
          <div className="flex-1 rounded-xl overflow-hidden border border-border shadow-md">
            <FieldMap />
          </div>
        </div>

        {/* SIDEBAR */}
        <div className="flex flex-col gap-6 overflow-hidden">

          {/* FLEET STATUS */}
          <Card className="flex-shrink-0">
            <CardHeader className="py-4">
              <CardTitle className="text-base font-semibold">Fleet Status</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {drones.map(d => (
                <div key={d.id} className="flex items-center justify-between text-sm">
                  <div className="flex items-center gap-2">
                    <span className="font-medium w-8 text-text-secondary">{d.id}</span>
                    <Battery className="w-4 h-4 text-accent-green" />
                    <span className="w-8">{Math.round(d.battery)}%</span>
                  </div>
                  <Badge variant={d.status === 'Returning' ? 'secondary' : 'default'} className="w-24 justify-center text-xs">
                    {d.status}
                  </Badge>
                </div>
              ))}
              <div className="h-px bg-border my-2"></div>
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2">
                  <span className="font-medium w-8 text-text-secondary">{rover.id}</span>
                  <BatteryCharging className="w-4 h-4 text-white" />
                  <span className="w-8">{Math.round(rover.battery)}%</span>
                </div>
                <Badge variant={rover.status === 'Idle' ? 'secondary' : 'default'} className="w-24 justify-center bg-blue-600 text-white text-xs">
                  {rover.status}
                </Badge>
              </div>
            </CardContent>
          </Card>

          {/* TASKS */}
          <Card className="flex-1 flex flex-col overflow-hidden">
            <CardHeader className="py-4 border-b border-border bg-background/50">
              <CardTitle className="text-base font-semibold">Task Console</CardTitle>
            </CardHeader>
            <CardContent className="p-0 flex-1 overflow-auto">
              <Tabs defaultValue="pending" className="w-full h-full flex flex-col">
                <div className="px-4 py-2 bg-background border-b border-border">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="pending">Pending ({tasks.filter(t => t.status === 'Pending').length})</TabsTrigger>
                    <TabsTrigger value="active">Active ({tasks.filter(t => t.status === 'In Progress').length})</TabsTrigger>
                  </TabsList>
                </div>
                <TabsContent value="pending" className="p-4 m-0 flex-1 overflow-auto space-y-4">
                  {tasks.filter(t => t.status === 'Pending').map(t => (
                    <div key={t.id} className="p-4 rounded-lg bg-card border border-border shadow-sm">
                      <div className="flex justify-between items-start mb-2">
                        <h4 className="font-medium text-sm text-white">{t.title}</h4>
                        <Badge variant="destructive" className="bg-alert-red/20 text-alert-red border-alert-red/50 text-[10px]">
                          {t.priority}
                        </Badge>
                      </div>
                      <p className="text-xs text-text-secondary mb-4 flex items-center gap-1">
                        <MapIcon className="w-3 h-3" /> Zone {t.zone}
                      </p>
                      <div className="flex gap-2">
                        <Button size="sm" className="w-full bg-accent-green text-bg-primary hover:bg-emerald-400 h-8 text-xs" onClick={() => approveTask(t.id)}>
                          Dispatch Rover
                        </Button>
                      </div>
                    </div>
                  ))}
                  {tasks.filter(t => t.status === 'Pending').length === 0 && (
                    <div className="text-center text-text-muted text-sm py-8">No pending tasks</div>
                  )}
                </TabsContent>
                <TabsContent value="active" className="p-4 m-0">
                  {tasks.filter(t => t.status === 'In Progress').map(t => (
                    <div key={t.id} className="p-4 rounded-lg bg-card border border-border shadow-sm border-l-4 border-l-blue-500">
                      <h4 className="font-medium text-sm text-white mb-1">{t.title}</h4>
                      <p className="text-xs text-text-secondary">Executing in Zone {t.zone}</p>
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